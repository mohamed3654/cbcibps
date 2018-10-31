# -*- coding: utf-8 -*-

from flask import render_template, request, jsonify, redirect, url_for

from datetime import datetime
from dateutil import parser

from BankChatBot import app
from BankChatBot import intents

import os
import json
import operator
import re
import random
import time
import csv
import sqlite3

#conn = sqlite3.connect(connString2")

# try:
#     conn.execute('''CREATE TABLE ERRORS
#            (SEARCH_WORD TEXT NOT NULL)''')
#     print "Table created successfully";
# except:
#     pass
#
# conn.close()
connString = "E:\\Work\\cbcibps\\BankChatBot\\datab\\customer.db"
connString2 = "E:\\Work\\cbcibps\\BankChatBot\\datab\\test.db"
conn = sqlite3.connect(connString)
c = conn.cursor()
def create_table():
   c.execute('''CREATE TABLE IF NOT EXISTS registeration (fname TEXT NOT NULL, lname TEXT NOT NULL, company TEXT NOT NULL, email TEXT NOT NULL,
		   phone REAL NOT NULL, account_type TEXT NOT NULL, products TEXT NOT NULL, Branchs TEXT NOT NULL, gender TEXT NOT NULL )''')
# print "Table created successfully";
#except:
    #pass
#conn.close()

# conn = sqlite3.connect(connString2")
#
# try:
#     conn.execute('''CREATE TABLE ERRORS
#            (SEARCH_WORD TEXT NOT NULL)''')
#     print "Table created successfully";
# except:
#     pass
#
# conn.close()
# # Reading Checking Account from external csv
# CheckingAccount = []
# with open("CheckingAccount.csv") as f:
#     CheckingAccount = [{k: str(v) if k == u"Description" or k == u"Date" else float(v) for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
#
#
# # Reading Savings Account from external csv
# SavingsAccount = []
# with open("SavingsAccount.csv") as f:
#     SavingsAccount = [{k: str(v) if k == u"Description" or k == u"Date" else str(v) for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]

#DefaultCurrency = u"Dirhams"
#DefaultRate = 1.0

# #CurrencyRates = [{ u"name": u"Dirhams", u"name_ar": u"درهم", u"value": 1.0 },
#                  { u"name": u"Dollars", u"name_ar": u"دولار", u"value": 0.27 },
#                  { u"name": u"Euro", u"name_ar": u"يورو", u"value": 0.23 }]

Months = [{ u"name": u"January", u"name_ar": u"يناير" }, { u"name": u"February", u"name_ar": u"فبراير" }, { u"name": u"March", u"name_ar": u"مارس" }, { u"name": u"April", u"name_ar": u"أبريل" },
          { u"name": u"May", u"name_ar": u"مايو" }, { u"name": u"June", u"name_ar": u"يونيو" }, { u"name": u"July", u"name_ar": u"يوليو" }, { u"name": u"August", u"name_ar": u"أغسطس" }, 
          { u"name": u"September", u"name_ar": u"سبتمبر" }, { u"name": u"October", u"name_ar": u"أكتوبر" }, { u"name": u"November", u"name_ar": u"نوفمبر" }, { u"name": u"December", u"name_ar": u"ديسمبر" }]
questions_list = []
answers_list = []
similarity_threshold = 0.6

@app.route("/")
@app.route("/home")
def home():
    #with open("bag_of_intents.json", "r") as f:
    #    intents.bag_of_intents = json.load(f)

    #f = open("bag_of_intents.json", "r")
    #intents.bag_of_intents = json.load(f)
    #keys = f.read()
    #print(str(keys))
    #keys = keys.decode("utf-8")
    #intents.bag_of_intents = json.loads(keys)
    #f.close()

    #if os.path.isfile("bag_of_intents.json"):
    #    os.remove("bag_of_intents.json")

    #f = open("bag_of_intents.json","w")
    #json.dump(intents.bag_of_intents, f, ensure_ascii=False)
    #f.close()

    sample = [u"I want to know the branch working hours",u"when will the branch open and close ?",u"I Have a Problem",u"I want to take loan"]

    return render_template("index.html",
        title="Home Page",
        sample=sample,
        year=datetime.now().year)

@app.route("/statement")
def statement():
    return render_template("statement.html",
        title="Account Statement",
        CheckingAccount=CheckingAccount,
        SavingsAccount=SavingsAccount,
        year=datetime.now().year)

@app.route("/registration")
def registration():
    return render_template("registaration.html",
        title="Registration")

@app.route("/registration_ar")
def registration_ar():
    return render_template("registaration_ar.html",
        title="Registration")


@app.route("/registerform", methods=["POST"])
def register_form():

    fnames = request.args.get("fname")
    fnames.encode("utf-8")
    lnames = request.args.get("lname")
    lnames.encode("utf-8")
    emails = request.args.get("email")
    emails.encode("utf-8")
    phones = request.args.get("phone")
    phones.encode("utf-8")
    companys = request.args.get("company")
    companys.encode("utf-8")
    account_types = request.args.get("account_type")
    account_types.encode("utf-8")
    productss = request.args.get("products")
    productss.encode("utf-8")
    Branchss = request.args.get("branchs")
    Branchss.encode("utf-8")
    genders = request.args.get("gender")
    genders.encode("utf-8")

    r_c = reg_class(fnames,lnames,emails,phones,companys,account_types,productss,Branchss,genders)
    conn = sqlite3.connect(connString)
    c = conn.cursor()
    c.execute(
        "INSERT INTO registeration (fname,lname,email,phone,company,account_type,products,Branchs,gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(fnames,lnames,emails, phones, companys, account_types, productss, Branchss, genders))
    conn.commit()
    c.close()
    conn.close()
    return jsonify(saved="success")
create_table()


@app.route("/process_question", methods=["POST"])
def process_question():
    question = request.args.get(u"question")
    question.encode("utf-8")

    answer = ""
    chart_type = ""
    expected_questions = ""
    data = []
    chart_title = ""
    tooltip = ""

    bad_question = [u"I didn't get that,Can you help me to understand you more?", u"Sorry, can you tell me again?", u"Sorry, can you say that again?",
                    u"I'm afraid I don't understand."]
    bad_question_ar = [u"عفواً, لم أفهم سيادتكم", u"آسف هل يمكنك السؤال مرة أخرى", u"لم أفهم السؤال سيدي", u"أخشى أني لم أفهم حضرتكم"]

    # Very long question or not English one => bad question
    if len(question) > 70:
        answer = bad_question[random.randint(0, len(bad_question) - 1)] if not intents.is_arabic(question) else bad_question_ar[random.randint(0, len(bad_question_ar) - 1)]
        #conn = sqlite3.connect("D:\\Work\\test\\Bank-ChatBot-with-DB\\Bank-ChatBot-master\\BankChatBot\\datab\\test.db")
        #print ('take')
        conn = sqlite3.connect(connString2)
        conn.execute("INSERT INTO ERRORS (SEARCH_WORD) \
                              VALUES (?)", [question])
        conn.commit()
        conn.close()
        return jsonify(question=question, answer=answer, similarity="")

    # print dynamic answer
    similarity = intents.get_all_similarity(question)
    if similarity[0][u"value"] < similarity_threshold:
        answer = bad_question[random.randint(0, len(bad_question) - 1)] if not intents.is_arabic(question) else bad_question_ar[random.randint(0, len(bad_question_ar) - 1)]
        #print ('taket')
        conn = sqlite3.connect(connString2)
        conn.execute("INSERT INTO ERRORS (SEARCH_WORD) \
                     VALUES (?)", [question])
        conn.commit()
        conn.close()
        return jsonify(question=question, answer=answer, similarity=similarity)

    for intt in intents.bag_of_intents:
        if intt[u"intent"] == similarity[0][u"intent"]:
            if not intents.is_arabic(question):
                answer = intt[u"answers"][random.randint(0, len(intt[u"answers"]) - 1)]
            else:
                answer = intt[u"answers_ar"][random.randint(0, len(intt[u"answers_ar"]) - 1)]
            break
    
    # global DefaultCurrency
    # global DefaultRate
    #
    # # Change Default Currency
    # if question.lower().find(u"dollar") >= 0 or question.lower().find(u"usd") >= 0 or question.find(u"دولار") >= 0:
    #     DefaultCurrency = u"Dollars" if not intents.is_arabic(question) else u"دولار"
    # elif question.lower().find(u"euro") >= 0 or question.find(u"يورو") >= 0:
    #     DefaultCurrency = u"Euro" if not intents.is_arabic(question) else u"يورو"
    # elif question.lower().find(u"dirham") >= 0 or question.lower().find(u"aed") >= 0 or question.find(u"درهم") >= 0:
    #     DefaultCurrency = u"Dirhams" if not intents.is_arabic(question) else u"درهم"
    #
    # for cur in CurrencyRates:
    #     if DefaultCurrency == cur[u"name"] or DefaultCurrency == cur[u"name_ar"]:
    #         DefaultRate = cur[u"value"]
    #
    # if intents.is_arabic(question) and DefaultCurrency == u"Dirhams":
    #     DefaultCurrency = u"درهم"
    # elif not intents.is_arabic(question) and DefaultCurrency == u"درهم":
    #     DefaultCurrency = u"Dirhams"
    #
    # if intents.is_arabic(question) and DefaultCurrency == u"Dollars":
    #     DefaultCurrency = u"دولار"
    # elif not intents.is_arabic(question) and DefaultCurrency == u"دولار":
    #     DefaultCurrency = u"Dollars"
    #
    # if intents.is_arabic(question) and DefaultCurrency == u"Euro":
    #     DefaultCurrency = u"يورو"
    # elif not intents.is_arabic(question) and DefaultCurrency == u"يورو":
    #     DefaultCurrency = u"Euro"
    #
    # # print Checking Account
    # if similarity[0][u"intent"] == u"balance_checking_account":
    #     answer += str(round(CheckingAccount[len(CheckingAccount) - 1][u"Balance"] * DefaultRate, 2)) + " " + DefaultCurrency
    #
    # # print Savings Account
    # if similarity[0][u"intent"] == u"balance_savings_account":
    #     answer += str(round(SavingsAccount[len(SavingsAccount) - 1][u"Balance"] * DefaultRate, 2)) + " " + DefaultCurrency
    #
    # # print expenses
    # if similarity[0][u"intent"] == u"expenses":
    #     monthly = 0.0
    #     total = 0.0
    #     startmonth = 1
    #     for stat in CheckingAccount:
    #         if parser.parse(stat["Date"], dayfirst=True).month != startmonth:
    #             data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #             startmonth = parser.parse(stat["Date"], dayfirst=True).month
    #             monthly = 0.0
    #
    #         if stat["Description"].find(u"expense") >= 0:
    #             total += stat["Debit"]
    #             monthly += stat["Debit"]
    #
    #     data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #     answer += str(round(total * DefaultRate, 2)) + u" " + DefaultCurrency
    #
    #     chart_title = u"Total Expenses" if not intents.is_arabic(question) else u"إجمالي المصروفات"
    #     tooltip = DefaultCurrency
    #     if question.find(u"bar") >= 0:
    #         chart_type = u"bar"
    #     elif question.find(u"pie") >= 0:
    #         chart_type = u"pie"
    #     elif question.find(u"donut") >= 0:
    #         chart_type = u"donut"
    #
    # # print withdraw
    # if similarity[0][u"intent"] == u"withdraw":
    #     monthly = 0.0
    #     total = 0.0
    #     startmonth = 1
    #     for stat in CheckingAccount:
    #         if parser.parse(stat["Date"], dayfirst=True).month != startmonth:
    #             data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #             startmonth = parser.parse(stat["Date"], dayfirst=True).month
    #             monthly = 0.0
    #
    #         if stat["Description"].find(u"withdraw") >= 0:
    #             total += stat["Debit"]
    #             monthly += stat["Debit"]
    #
    #     data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #     answer += str(round(total * DefaultRate, 2)) + u" " + DefaultCurrency
    #
    #     chart_title = u"Total Withdraws" if not intents.is_arabic(question) else u"السحب النقدي"
    #     tooltip = DefaultCurrency
    #     if question.find(u"bar") >= 0:
    #         chart_type = u"bar"
    #     elif question.find(u"pie") >= 0:
    #         chart_type = u"pie"
    #     elif question.find(u"donut") >= 0:
    #         chart_type = u"donut"
    #
    # # print loans
    # if similarity[0]["intent"] == u"loans":
    #     monthly = 0.0
    #     total = 0.0
    #     startmonth = 1
    #     for stat in CheckingAccount:
    #         if parser.parse(stat[u"Date"], dayfirst=True).month != startmonth:
    #             data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #             startmonth = parser.parse(stat["Date"], dayfirst=True).month
    #             monthly = 0.0
    #
    #         if stat[u"Description"].find(u"loans") >= 0:
    #             total += stat[u"Debit"]
    #             monthly += stat[u"Debit"]
    #
    #     data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #     answer += str(round(total * DefaultRate, 2)) + u" " + DefaultCurrency
    #
    #     chart_title = u"Total Loans" if not intents.is_arabic(question) else u"إجمالي الأقساط"
    #     tooltip = DefaultCurrency
    #     if question.find(u"bar") >= 0:
    #         chart_type = u"bar"
    #     elif question.find(u"pie") >= 0:
    #         chart_type = u"pie"
    #     elif question.find(u"donut") >= 0:
    #         chart_type = u"donut"
    #
    # # print car
    # if similarity[0]["intent"] == u"car":
    #     monthly = 0.0
    #     total = 0.0
    #     startmonth = 1
    #     for stat in CheckingAccount:
    #         if parser.parse(stat[u"Date"], dayfirst=True).month != startmonth:
    #             data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #             startmonth = parser.parse(stat[u"Date"], dayfirst=True).month
    #             monthly = 0.0
    #
    #         if stat[u"Description"].lower().find(u"car") >= 0:
    #             total += stat[u"Debit"]
    #             monthly += stat[u"Debit"]
    #
    #     data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #     answer += str(round(total * DefaultRate, 2)) + u" " + DefaultCurrency
    #
    #     chart_title = u"Car Expenditure" if not intents.is_arabic(question) else u"مصروفات السيارة"
    #     tooltip = DefaultCurrency
    #     if question.find(u"bar") >= 0:
    #         chart_type = u"bar"
    #     elif question.find(u"pie") >= 0:
    #         chart_type = u"pie"
    #     elif question.find(u"donut") >= 0:
    #         chart_type = u"donut"
    #
    # # print food
    # if similarity[0][u"intent"] == u"food":
    #     monthly = 0.0
    #     total = 0.0
    #     startmonth = 1
    #     for stat in CheckingAccount:
    #         if parser.parse(stat[u"Date"], dayfirst=True).month != startmonth:
    #             data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #             startmonth = parser.parse(stat[u"Date"], dayfirst=True).month
    #             monthly = 0.0
    #
    #         if stat[u"Description"].lower().find(u"food") >= 0:
    #             total += stat[u"Debit"]
    #             monthly += stat[u"Debit"]
    #
    #     data.append({u"name": Months[startmonth - 1][u"name" if not intents.is_arabic(question) else u"name_ar"], u"count": round(monthly * DefaultRate, 2)})
    #     answer += str(round(total * DefaultRate, 2)) + u" " + DefaultCurrency
    #
    #     chart_title = u"Food Expenditure" if not intents.is_arabic(question) else u"مصروفات الطعام والشراب"
    #     tooltip = DefaultCurrency
    #     if question.find(u"bar") >= 0:
    #         chart_type = u"bar"
    #     elif question.find(u"pie") >= 0:
    #         chart_type = u"pie"
    #     elif question.find(u"donut") >= 0:
    #         chart_type = u"donut"
    #
    questions_list.append(question)
    answers_list.append(answer)



    return jsonify(question=question,
                   unique_id=str(datetime.now().year) + "_" + str(datetime.now().month) + "_" + str(datetime.now().day) + "_" + str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second),
                   data=data,
                   chart_title=chart_title,
                   tooltip=tooltip,
                   chart_type=chart_type,
                   answer=answer,
                   similarity=similarity)

class reg_class :
    def __init__(self, fname,lname,email, phone, company, account_type, products, Branchs, gender):
        """Return a Customer object whose name is *name*."""
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.company = company
        self.account_type = account_type
        self.products = products
        self.Branchs = Branchs
        self.gender = gender