# -*- coding: utf-8 -*-

from langdetect import detect

import operator
import json
import spacy

nlp = spacy.load("en")

arabic_letters = [u"ا", u"أ", u"آ", u"إ", u"ء", u"ب", u"ت", u"ـ", u"ث", u"ج", u"ح", u"خ", u"د", u"ذ", u"ر", u"ز", u"س", u"ش", u"ص",
                  u"ض", u"ط", u"ظ", u"ع", u"غ", u"ف", u"ق", u"ك", u"ل", u"م", u"ن", u"ه", u"و", u"ؤ", u"ة", u"ئ", u"ي", u"ي"]

#bag_of_intents = []
bag_of_intents = [{
                      u"intent": u"hi",

                      u"values": [u"hi", u"hello", u"welcome", u"what's up", u"hey", u"hay", u"hai", u"good morning", u"good afternoon", u"hai", u"good evening"],
                      u"keywords": [{u"key": u"hi", u"value": 1.5}, {u"key": u"hello", u"value": 1.5}, {u"key": u"hey", u"value": 1.5}, {u"key": u"hay", u"value": 1.5},
                                    {u"key": u"hai", u"value": 1.5}],
                      u"keywords_ar": [{u"key": u"هلا", u"value": 1.5}, {u"key": u"أهلا", u"value": 1.5}, {u"key": u"اهلا", u"value": 1.5}, {u"key": u"وسهلا", u"value": 1.5},
                                       {u"key": u"حيا", u"value": 1.0}, {u"key": u"حياكم", u"value": 1.0}, {u"key": u"مرحبا", u"value": 1.5}, {u"key": u"مرحب", u"value": 1.5},
                                       {u"key": u"السلام", u"value": 1.0}, {u"key": u"عليكم", u"value": 1.0}, {u"key": u"ورحمه", u"value": 1.0}, {u"key": u"رحمه", u"value": 1.0},
                                       {u"key": u"ورحمة", u"value": 1.0}, {u"key": u"رحمة", u"value": 1.0}, {u"key": u"الله", u"value": 1.0}, {u"key": u"وبركاته", u"value": 1.0},
                                       {u"key": u"بركاته", u"value": 1.0}, {u"key": u"وبركاتة", u"value": 1.0}, {u"key": u"بركاتة", u"value": 1.0},
									   {u"key": u"يا", u"value": 1.5}, {u"key": u"صباح", u"value": 1.0}, {u"key": u"الخير", u"value": 2.0}],
                      u"answers": [u"Welcome to BankBot by CIB, How can I serve you ?",u"Welcome, Thanks for choosing BankBot by CIB,How can I help you ?"],
                      u"answers_ar": [u"مرحبا بك, كيف أستطيع خدمتك ؟", u"أهلا وسهلا, كيف أستطيع خدمتك ؟"]
                  },
            {
        u"intent": u"how_are_you",

        u"values": [u"how are you", u"how are you ?", u"hi, how are you ?", u"hello, how are you ?",
                    u"hello, how r u ?", u"hi, how r u ?", u"how r u", u"how r u ?"],
        u"keywords_ar": [{u"key": u"كيف", u"value": 1.5}, {u"key": u"حالك", u"value": 1.5},
                         {u"key": u"شلونك", u"value": 1.5}, {u"key": u"شو", u"value": 1.5},
                         {u"key": u"وشو", u"value": 1.5}, {u"key": u"اخبارك", u"value": 1.5},
                         {u"key": u"أخبارك", u"value": 1.5}, {u"key": u"عساكم", u"value": 1.0},
                         {u"key": u"عساك", u"value": 1.0}, {u"key": u"بخير", u"value": 1.5},
                         {u"key": u"أنت", u"value": 1.0}, {u"key": u"انت", u"value": 4.0},
                         {u"key": u"إنت", u"value": 1.0}, {u"key": u"أزيك", u"value": 1.5},
                         {u"key": u"ازيك", u"value": 1.5}, {u"key": u"إزيك", u"value": 1.5},
                         {u"key": u"عامل", u"value": 4.0}, {u"key": u"ايه", u"value": 1.0},
                         {u"key": u"إيه", u"value": 1.0}, {u"key": u"أيه", u"value": 1.0},
                         {u"key": u"كويس", u"value": 3.5}, {u"key": u"يا", u"value": 1.0}],
             u"answers": [u"Doing great, thanks ,How can I help you ?", u"I am fine thank you ,How can I help you ?",
                     u"Fine,How can I help you ?", u"Feeling wonderful!,how can I help you ?"],
             u"answers_ar": [u"أنا بخير, شكراً لك, كيف أستطيع مساعدتك", u"الحمد لله أنا بخير, كيف أستطيع مساعدتك !", u"شكراً, كيف أستطيع مساعدتك",
                        u"شكراً, كيف أستطيع خدمتك", u"شكرا جزيلا, كيف يمكنني مساعدتك", u"أشكرك , كيف أستطيع مساعدتك "]
                        },
                     {
                         u"intent": u"thanks",

                         u"values": [u"thanks", u"thank you so much", u"thank you, you are the best",
                                     u"many thanks to you", u"thank you, you are the best bank",u"you are good",
                                     u"you are so good", u"you are very clever", u"thank you", u"thank u", u"thnx ",
                                     u"many thanks",u"you are smart"
                                     u"Thank you so much", u"thankful", u"grateful", u"glade to see you"],

                         u"keywords_ar": [
                             {u"key": u"شكرا", u"value": 1.5}, {u"key": u"شكر", u"value": 1.5},
                             {u"key": u"شاكر", u"value": 1.5}, {u"key": u"مشكور", u"value": 1.5},
                             {u"key": u"اشكرك", u"value": 1.5}, {u"key": u"أشكرك", u"value": 1.5},
                             {u"key": u"إشكرك", u"value": 1.5}, {u"key": u"متشكر", u"value": 1.5},
                             {u"key": u"شكر", u"value": 1.5}, {u"key": u"متشكرين", u"value": 1.5},
                             {u"key": u"أوي", u"value": 1.5}, {u"key": u"جدا", u"value": 2.5},
                             {u"key": u"أوى", u"value": 1.5}, {u"key": u"اوي", u"value": 1.5},
                             {u"key": u"اوى", u"value": 1.5}, {u"key": u"إوى", u"value": 1.5},
                             {u"key": u"إوي", u"value": 1.5}, {u"key": u"فعلا", u"value": 1.5},
                             {u"key": u"تحية", u"value": 1.5}, {u"key": u"تحياتي", u"value": 1.5},
                             {u"key": u"سررت", u"value": 1.5}, {u"key": u"بك", u"value": 1.0},
                             {u"key": u"سعدت", u"value": 1.5}, {u"key": u"جدا", u"value": 1.5},
                             {u"key": u"جزيلا", u"value": 1.5}, {u"key": u"يا", u"value": 1.0},
                             {u"key": u"ربنا", u"value": 1.5}, {u"key": u"يخليك", u"value": 1.5},
                             {u"key": u"يكرمك", u"value": 1.5}, {u"key": u"ألف", u"value": 1.0},
                             {u"key": u"أحسن", u"value": 2.5}, {u"key": u"احسن", u"value": 2.5},
                             {u"key": u"خدمة", u"value": 2.5},
                             {u"key": u"مع", u"value": 1.5}, {u"key": u"محترم", u"value": 4.5},
                             {u"key": u"سى", u"value": 1.5}, {u"key": u"اي", u"value": 1.5},
                             {u"key": u"بي ", u"value": 1.5},{u"key": u"عملاء ", u"value": 3.5},
							 {u"key": u"عملا", u"value": 3.5},

                             {u"key": u"ان", u"value": 1.5}, {u"key": u"شاء", u"value": 1.5},
                             {u"key": u"الله ", u"value": 2.0}, {u"key": u"والله", u"value": 2.0},
                             {u"key": u"العظيم", u"value": 1.5}, {u"key": u"بنك", u"value": 2.5},
                             {u"key": u"نثق", u"value": 4.5}, {u"key": u"ناس", u"value": 2.5},
                             {u"key": u"وناس", u"value": 2.5}, {u"key": u"انتوا", u"value": 1.5},
                             {u"key": u"فيه", u"value": 3.5}, {u"key": u"عندكم", u"value": 3.5},
                             {u"key": u"محترمة", u"value": 2.5},
                             {u"key": u"فروع", u"value": 3.5}, {u"key": u"فى", u"value": 3.5},
                             {u"key": u"جميع", u"value": 2.5}, {u"key": u"أنحاء", u"value": 3.5},
                             {u"key": u"العالم", u"value": 2.0}, {u"key": u"CIB", u"value": 2.0},
                             {u"key": u"ممتازة", u"value": 3.0}, {u"key": u"متميزه", u"value": 3.0},
                             {u"key": u"جميل", u"value": 2.0}],

         u"answers": [u"We thank you for your precious trust in the bank and we hope that we will always have your satisfaction and trust "],
         u"answers_ar": [u"نشكر حضرتك على ثقتك الغالية في البنك ونتمنى أن ننال دائماً رضا وثقة حضرتك"]
                },
                     {u"intent": u"nastiness",

                            u"values": [u"you are the worst", u"you are the worst bank",
                                  u"fuck you",u"you are bad",u"you are so bad",u"you are crazy",
                                  u"you are too bad", u"fuck you son of the pitch", u"your are stupid"],
                            u"keywords_ar": [
                                  {u"key": u"اوسخ", u"value": 4.5}, {u"key": u"أوسخ", u"value": 4.5},
                                  {u"key": u"أوي", u"value": 1.5}, {u"key": u"جدا", u"value": 2.5},
                                  {u"key": u"أوى", u"value": 1.5}, {u"key": u"اوي", u"value": 1.5},
                                  {u"key": u"اوى", u"value": 1.5}, {u"key": u"إوى", u"value": 1.5},
                                  {u"key": u"إوي", u"value": 1.5}, {u"key": u"فعلا", u"value": 1.5},
                                  {u"key": u"افشل", u"value": 3.5}, {u"key": u"جدا", u"value": 1.5},
                                  {u"key": u"يا", u"value": 1.0}, {u"key": u"اتعملت", u"value": 2.5},
                                  {u"key": u"ربنا", u"value": 1.5}, {u"key": u"يخدك", u"value": 3.5},
                                  {u"key": u"اسوء", u"value": 4.5}, {u"key": u"أسوء", u"value": 4.5},
                                  {u"key": u"خدمة", u"value": 3.5}, {u"key": u"أسوأ", u"value": 4.5},
                                  {u"key": u"مع", u"value": 1.5}, {u"key": u"فاشل", u"value": 4.5},
                                  {u"key": u"سى", u"value": 1.5}, {u"key": u"اي", u"value": 1.5},
                                  {u"key": u"بي ", u"value": 1.5}, {u"key": u"عملاء ", u"value": 3.5},
                                  {u"key": u"عملا", u"value": 3.5}, {u"key": u"معاه", u"value": 2.5},
                                  {u"key": u"على", u"value": 2.5}, {u"key": u"عدم", u"value": 2.5},
                                  {u"key": u"تعاونكم", u"value": 3.5}, {u"key": u"لا", u"value": 2.5},
                                  {u"key": u"مفيش", u"value": 3.5}, {u"key": u"من", u"value": 2.5},
                                  {u"key": u"كدة", u"value": 2.5},{u"key": u"ابن", u"value": 2.5},
                                  {u"key": u"بنك", u"value": 2.5}, {u"key": u"وإدارة", u"value": 2.5},
                                  {u"key": u"نثق", u"value": 4.5}, {u"key": u"ناس", u"value": 2.5},
                                  {u"key": u"وناس", u"value": 2.5}, {u"key": u"انتوا", u"value": 1.5},
                                  {u"key": u"فيه", u"value": 3.5}, {u"key": u"عندكم", u"value": 3.5},
                                  {u"key": u"وسخة", u"value": 4.5}, {u"key": u"ف", u"value": 2.5},
                                  {u"key": u"غبى", u"value": 4.5}, {u"key": u"مجنون", u"value": 4.5},
                                  {u"key": u"اهبل", u"value": 4.5}, {u"key": u"انت", u"value": 2.5},
                                  {u"key": u"متخلف", u"value": 4.5}, {u"key": u"كلب", u"value": 4.5},
                                  {u"key": u"متخلفين", u"value": 4.5}, {u"key": u"هبل", u"value": 4.5},
                                  {u"key": u"يابنى", u"value": 2.5}, {u"key": u"يبنى", u"value": 2.5},
                                  {u"key": u"فروع", u"value": 3.5}, {u"key": u"فى", u"value": 3.5},
                                  {u"key": u"جميع", u"value": 2.5}, {u"key": u"أنحاء", u"value": 3.5},
                                  {u"key": u"العالم", u"value": 2.0}, {u"key": u"CIB", u"value": 2.0},
                                  {u"key": u"وسخ", u"value": 4.5}, {u"key": u"مصر", u"value": 2.0},
                                  {u"key": u"إدارة", u"value": 2.5},{u"key": u"يخدكوا", u"value": 4.0}],

                 u"answers": [u"We apologize that you did not receive the required service level. Please provide us with the details of your problem by dialing 19666 so we can solve the issue"],
                 u"answers_ar":[u"نعتذر عن عدم حصول حضرتك على مستوى الخدمة المطلوبة. الرجاء تزويدنا بتفاصيل المشكلة التى تواجه سيادتكم من خلال الاتصال على 19666 حتى نستطيع حل المشكلة"]

            },
              {
                u"intent": u"open_account",

                        u"values": [u"what are the documents needed to make account?", u"i want to open a debit card", u"i want to open a current account",
                        u"i want to take a debit card",u"i want to take a current account"
                        u"i need to open saving account", u"i want to open account", u"i want to make account",u"i want to take a credit card",
                        u"how much is the intrest of the saving account?", u"what is the types of saving account?",
                        u"what is the documents needed to make account?", u"need a account", u"saving account",
                        u"debit account",u"current account",u"i want more information about saving account",
                        u"how much intrest of the saving account?", u"i want to know the interset of the saving account"
                    ],
                 u"keywords": [{u"key": u"debit account", u"value": 5.0}, {u"key": u"saving account", u"value": 5.0},{u"key": u"current account", u"value": 5.0}],
                    u"keywords_ar": [

                            {u"key": u"ايه", u"value": 3.0}, {u"key": u"اية", u"value": 3.0}, {u"key": u"امتى", u"value": 3.0},
                            {u"key": u"ازاى", u"value": 3.0},{u"key": u"ممكن", u"value": 3.0}, {u"key": u"كام", u"value": 3.0},
                            {u"key": u"هل", u"value": 3.0},

                            {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0}, {u"key": u"لدي", u"value": 3.0},
                            {u"key": u"عندي", u"value": 4.0}, {u"key": u"عندكوا", u"value": 3.0}, {u"key": u"عم", u"value": 3.0},
                            {u"key": u"لما", u"value": 3.5}, {u"key": u"مني", u"value": 3.5},{u"key": u"جماعة", u"value": 4.0},
                            {u"key": u"انتوا", u"value": 3.0},{u"key": u"لانى", u"value": 3.0},{u"key": u"كلهم", u"value": 3.5},
                            {u"key": u"اخويا", u"value": 3.0},

                            {u"key": u"عايز", u"value": 3.5}, {u"key": u"عاوز", u"value": 3.5},  {u"key": u"اشترك", u"value": 4.0},
                            {u"key": u"اعرف", u"value": 3.5},{u"key": u"اقدم", u"value": 4.5},{u"key": u"اتصلت", u"value": 4.0},
                            {u"key": u"اعمل", u"value": 3.5}, {u"key": u"اخد", u"value": 3.0}, {u"key": u"تقولى", u"value": 3.0},
                            {u"key": u"بتتحسب", u"value": 4.0},{u"key": u"بتحسبوا", u"value": 4.0},{u"key": u"متاح", u"value": 3.0},
                            {u"key": u"محتاج", u"value": 3.0},{u"key": u"ينفع", u"value": 3.0},{u"key": u"عامل", u"value": 3.0},
                            {u"key": u"بستفسر", u"value": 3.0}, {u"key": u"كنت", u"value": 3.0}, {u"key": u"بسئل", u"value": 3.0},
                            {u"key": u"سمحت", u"value": 2.0}, {u"key": u"تبقى", u"value": 3.0}, {u"key": u"يوجد", u"value": 4.5},
                            {u"key": u"يساعدنى", u"value": 4.0},{u"key": u"بلاقي", u"value": 3.5},{u"key": u"تساعدنى", u"value": 4.0},
                            {u"key": u"اشترك", u"value": 4.0}, {u"key": u"بحاول", u"value": 4.0}, {u"key": u"طلب", u"value": 4.0},
                            {u"key": u"اقرب", u"value": 4.5},{u"key": u"عارف", u"value": 4.5}, {u"key": u"قادر", u"value": 3.5},
                            {u"key": u"يفتح", u"value": 4.0}, {u"key": u"افتح", u"value": 4.0}, {u"key": u"اشتركت", u"value": 4.0},
                            {u"key": u"اطلب", u"value": 4.0}, {u"key": u"يساعدنى", u"value": 4.0},


                            {u"key": u"على", u"value": 4.5}, {u"key": u"قد", u"value": 3.0}, {u"key": u"لو", u"value": 2.0},
                            {u"key": u"عن", u"value": 3.0},{u"key": u"لسه", u"value": 3.0},{u"key": u"فى", u"value": 4.5},
                            {u"key": u"الى", u"value": 3.0}, {u"key": u"عليها", u"value": 3.5}, {u"key": u"دى", u"value": 3.0},


                            {u"key": u"كارت", u"value": 4.0}, {u"key": u"حساب", u"value": 4.5}, {u"key": u"جارى", u"value": 5.0},
                            {u"key": u"توفير", u"value": 5.0},{u"key": u"اكونت", u"value": 4.0}, {u"key": u"نظام", u"value": 3.0},
                            {u"key": u"انواع", u"value": 3.5},{u"key": u"السى اى بى", u"value": 3.0},
                            {u"key": u"الفرع", u"value": 4.5}, {u"key": u"نسبة", u"value": 4.5},
                            {u"key": u"الورق", u"value": 4.5}, {u"key": u"المطلوب", u"value": 4.5}, {u"key": u"الفايدة", u"value": 4.5},
                            {u"key": u"الاجرأت", u"value": 4.5}, {u"key": u"اجراء", u"value": 4.5}, {u"key": u"عاجل", u"value": 4.0},
                            {u"key": u"بنك", u"value": 4.0}, {u"key": u"الatms", u"value": 4.0}, {u"key": u"atmال", u"value": 4.0},
                            {u"key": u"سى اي بى", u"value": 3.0}, {u"key": u"cib", u"value": 3.0}

        ],

        u"answers": [u''' For more information about Current Account you can visit the following link: <br/> <a href="https://www.cibeg.com/english/Personal/Accounts/Pages/CurrentAccount.aspx/" target="_blank"> https://www.cibeg.com/english/Personal/Accounts/Pages/CurrentAccount.aspx </a><br/>
        			 and For more information about saving Account  you can visit the following link: <br/> <a href="https://www.cibeg.com/english/Personal/Accounts/Pages/SavingAccount.aspx/" target="_blank"> https://www.cibeg.com/english/Personal/Accounts/Pages/SavingAccount.aspx </a><br/>
	                 and You can register your data by visiting the following link:  <br/><a href=" http://localhost:5555/registration" target="_blank" > Registration </a> <br/>  and one of our representitives will contact you '''],

         u"answers_ar": [u''' لمعلومات اكثر عن الحساب الجاري يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Accounts/Pages/CurrentAccount.aspx//" target="_blank"> https://www.cibeg.com/arabic/Personal/Accounts/Pages/CurrentAccount.aspx/</a><br/>
                            ولمعلومات اكثر عن حساب التوفير يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Accounts/Pages/SavingAccount.aspx//" target="_blank"> https://www.cibeg.com/arabic/Personal/Accounts/Pages/SavingAccount.aspx/</a><br/>
                                                 و يمكنك ايضأ تسجيل بياناتك و سوف يقوم احد ممثلى خدمة العملاء بالتواصل معك
                         <br/><a href=" http://localhost:5555/registration_ar" target="_blank" > تسجيل </a> <br/> ''']
                  },
      {
        u"intent": u"credit_card",

        u"values": [u"I want to take credit card", u"i want to take a credit card",u"what are the documents needed to take a credit card?",
                    u"what is the documents needed to take a credit card?",u"what is the papers needed to take a credit card?",
                    u"how much is the intrest of the credit card?",u"what are the documents needed to take a credit card?",
                    u"credit card", u"intrest", u"how much intrest of the credit card?",u"i want to know the interset of the credit card",
                    u"what is the types of credit card?",u"I want to take visa ", u"i want to take a visa ",
                    u"what are the documents needed to take a visa?",u"what is the documents needed to take a visa?",
                    u"what is the papers needed to take a visa?",u"how much is the intrest of the visa?",
                    u"what are the documents needed to take a visa?",u"visa", u"how much intrest of the visa?",
                    u"i want to know the interset of the visa",u"what is the types of visa?"
                    ],
        u"keywords": [{u"key": u"a credit card", u"value": 5.0},{u"key": u"credit card", u"value": 5.0}, {u"key": u"visa", u"value": 5.0}],
        u"keywords_ar": [{u"key": u"ايه", u"value": 3.0}, {u"key": u"امتى", u"value": 3.0},
                         {u"key": u"ازاى", u"value": 3.0},
                         {u"key": u"هل", u"value": 3.0}, {u"key": u"ممكن", u"value": 3.0},
                         {u"key": u"كام", u"value": 3.0},

                         {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0},

                         {u"key": u"عايز", u"value": 3.5}, {u"key": u"عاوز", u"value": 3.5},
                         {u"key": u"اعرف", u"value": 3.5}, {u"key": u"اقدم", u"value": 4.5},
                         {u"key": u"اعمل", u"value": 4.5}, {u"key": u"اخد", u"value": 3.0},
                         {u"key": u"تقولى", u"value": 3.0}, {u"key": u"بتتحسب", u"value": 4.0},
                         {u"key": u"بتحسبوا", u"value": 4.0}, {u"key": u"متاح", u"value": 3.0},
                         {u"key": u"محتاج", u"value": 3.0}, {u"key": u"ينفع", u"value": 3.0},
                         {u"key": u"بستفسر", u"value": 3.0}, {u"key": u"كنت", u"value": 3.0},
                         {u"key": u"بسئل", u"value": 3.0}, {u"key": u"عامل", u"value": 3.0},
                         {u"key": u"سمحت", u"value": 2.0}, {u"key": u"تبقى", u"value": 3.0},

                         {u"key": u"على", u"value": 4.5}, {u"key": u"قد", u"value": 3.0},
                         {u"key": u"لو", u"value": 2.0}, {u"key": u"عن", u"value": 3.0},
                         {u"key": u"مش", u"value": 4.0},

                         {u"key": u"نظام", u"value": 3.0}, {u"key": u"الفيزا", u"value": 5.0},
                         {u"key": u"الاءتمان", u"value": 5.0}, {u"key": u"الاءتمانية", u"value": 5.0},
                         {u"key": u"الأتمان", u"value": 5.0}, {u"key": u"الاتمان", u"value": 5.0},
                         {u"key": u"انواع", u"value": 3.5}, {u"key": u"card", u"value": 5.0},
                         {u"key": u"credit", u"value": 5.0}, {u"key": u"الvisa", u"value": 5.0},
                         {u"key": u"حساب", u"value": 4.0}, {u"key": u"الفرع", u"value": 4.5},
                         {u"key": u"نسبة", u"value": 4.0}, {u"key": u"بطاقة", u"value": 4.0},
                         {u"key": u"الورق", u"value": 4.5}, {u"key": u"المطلوب", u"value": 4.5},
                         {u"key": u"تمويل", u"value": 5.0},
                         {u"key": u"الاجرأت", u"value": 4.5}, {u"key": u"اجراء", u"value": 4.5},
                         {u"key": u"عاجل", u"value": 4.0},
                         {u"key": u"فيزا", u"value": 5.0}, {u"key": u"شخصي", u"value": 5.0},
                         {u"key": u"الفايدة", u"value": 4.5},
                         {u"key": u"بنك", u"value": 4.0}, {u"key": u"الatms", u"value": 4.0},
                         {u"key": u"atmال", u"value": 4.0},
                         {u"key": u"سى اي بى", u"value": 3.0}, {u"key": u"cib", u"value": 3.0},
                         {u"key": u"السى اى بى", u"value": 3.0}
                         ],

        u"answers": [u'''For more information about types of Credit Cards you can visit the following link: <br/> <a href="https://www.cibeg.com/english/Personal/Cards/Pages/default.aspx/" target="_blank"> https://www.cibeg.com/english/Personal/Cards/Pages/default.aspx </a> <br/>
					and You can register your data by visiting the following link:  <br/><a href=" http://localhost:5555/registration" target="_blank" > Registration </a> <br/>  and one of our representitives will contact you '''],

        u"answers_ar": [u''' :لمعرفة معلومات اكثر عن انواع الكروت الاْتمانية يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Cards/Pages/default.aspx/" target="_blank"> https://www.cibeg.com/arabic/Personal/Cards/Pages/default.aspx/</a> <br/>
							و يمكنك ايضأ تسجيل بياناتك و سوف يقوم احد ممثلى خدمة العملاء بالتواصل معك   	<br/><a href=" http://localhost:5555/registration_ar" target="_blank" > تسجيل </a> <br/> ''']
               },
                {
                      u"intent": u"loan",

                      u"values": [u"I want to take loan", u"i want to take a loan", u"what are the documents needed to take a loan?",
                                  u"what is the documents needed to take a loan?",u"what is the papers needed to take a loan?",
                                  u"how much is the intrest of the loan?",u"what is the documents needed to take a loan?",
                                  u"loan",u"loans",u"intrest",u"how much intrest of the loan?",u"i want to know the interset of the loan"
                                  u"what is the types of loans?"],
                      u"keywords": [{u"key": u"a loan", u"value": 5.0},{u"key": u"loan", u"value": 5.0}],
                      u"keywords_ar": [{u"key": u"ايه", u"value": 3.0},{u"key": u"امتى", u"value": 3.0},{u"key": u"ازاى", u"value": 3.0},
                                {u"key": u"هل", u"value": 3.0},{u"key": u"ممكن", u"value": 3.0},{u"key": u"كام", u"value": 3.0},

                                {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0},

                                {u"key": u"عايز", u"value": 3.5},{u"key": u"عاوز", u"value": 3.5}, {u"key": u"اعرف", u"value": 3.5},{u"key": u"اقدم", u"value": 4.5},
                                {u"key": u"اعمل", u"value": 3.0}, {u"key": u"اخد", u"value": 3.0}, {u"key": u"تقولى", u"value": 3.0},{u"key": u"بتتحسب", u"value": 4.0},
                                {u"key": u"بتحسبوا", u"value": 4.0},{u"key": u"متاح", u"value": 3.0},{u"key": u"محتاج", u"value": 3.0},{u"key": u"ينفع", u"value": 3.0},
                                {u"key": u"بستفسر", u"value": 3.0},{u"key": u"كنت", u"value": 3.0},{u"key": u"بسئل", u"value": 3.0},{u"key": u"عامل", u"value": 3.0},
                                {u"key": u"سمحت", u"value": 2.0},{u"key": u"تبقى", u"value": 3.0},

                                {u"key": u"على", u"value": 4.5},{u"key": u"قد", u"value": 3.0},{u"key": u"لو", u"value": 2.0},{u"key": u"عن", u"value": 3.0},
                                {u"key": u"مش", u"value": 4.0},{u"key": u"قرد", u"value": 4.0},

                                {u"key": u"نظام", u"value": 3.0}, {u"key": u"القروض", u"value": 5.0}, {u"key": u"انواع", u"value": 3.5},
                                {u"key": u"حساب", u"value": 4.0},{u"key": u"الفرع", u"value": 4.5},{u"key": u"نسبة", u"value": 4.0},
                                {u"key": u"الورق", u"value": 4.5},{u"key": u"المطلوب", u"value": 4.5},{u"key": u"تمويل", u"value": 5.0},
                                {u"key": u"الاجرأت", u"value": 4.5},{u"key": u"اجراء", u"value": 4.5},{u"key": u"عاجل", u"value": 4.0},
                                {u"key": u"قرض", u"value": 5.0},{u"key": u"شخصي", u"value": 5.0},{u"key": u"الفايدة", u"value": 4.5},
                                {u"key": u"بنك", u"value": 4.0}, {u"key": u"الatms", u"value": 4.0}, {u"key": u"atmال", u"value": 4.0},
                                {u"key": u"سى اي بى", u"value": 3.0},{u"key": u"cib", u"value": 3.0},{u"key": u"السى اى بى", u"value": 3.0}
                                      ],
                    u"answers": [u'''For more information about types of personal loans  you can visit the following link: <br/> <a href="https://www.cibeg.com/english/Personal/Loans/Pages/default.aspx/" target="_blank"> https://www.cibeg.com/english/Personal/Loans/Pages/default.aspx </a> <br/>  or  "Send SMS with the word 'loan' on 16644"
						   and you can calculate the lan monthly installment by visiting the following link: <br/> <a href="https://www.cibeg.com/English/Personal/Loans/Pages/Calculator.aspx/" target="_blank"> https://www.cibeg.com/English/Personal/Loans/Pages/Calculator.aspx </a> <br/>
						   and You can register your data by visiting the following link:  <br/><a href=" http://localhost:5555/registration" target="_blank" > Registration </a> <br/>  and one of our representitives will contact you '''],

                    u"answers_ar": [u''' :لمعرفة معلومات اكثر عن انواع القروض الشخصية يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Loans/Pages/default.aspx/" target="_blank"> https://www.cibeg.com/arabic/Personal/Loans/Pages/default.aspx</a> <br/> او أرسل كلمة “قرض “على رقم 16644
و يمكنك حساب التقسيط الشهرى للقرض من خلال زيارة هذا الرابط                                      	<br/> <a href="https://www.cibeg.com/arabic/Personal/Loans/Pages/Calculator.aspx/" target="_blank"> https://www.cibeg.com/arabic/Personal/Loans/Pages/Calculator.aspx </a> <br/>
                                              و يمكنك ايضأ تسجيل بياناتك و سوف يقوم احد ممثلى خدمة العملاء بالتواصل معك
                                      <br/><a href=" http://localhost:5555/registration_ar" target="_blank" > تسجيل </a> <br/> ''']

                },
                {
                 u"intent": u"CD_TD",

                    u"values": [u"what are the documents needed to make cd?",u"what are the documents needed to make td?",
                                u"what are the documents needed to make certificate of Deposit?",u"what are the documents needed to make Time Deposit?",
                                u"i want to make a cd", u"i want to make a TD",
                                u"i want to make a certificate of Deposit", u"i want to make a Time Deposit",
                                u"i want to take a cd",u"i want to take a td",
                                u"i want to take a certificate of Deposit",u"i want to take a Time Deposit",
                                u"i need to open cd", u"i want to open td",
                                u"i want to open a certificate of Deposit",u"i want to open a Time Deposit",
                                u"how much is the intrest of the cd?", u"how much is the intrest of the certificate of Deposit?",
                                u"how much is the intrest of the td?", u"how much is the intrest of the Time Deposit?",
                                u"what is the types of cd?",u"what is the types of td?",
                                u"what is the types of certificate?",u"what is the types of Time Deposit?",
                                u"need a cd", u"cd",u"need a certificate of Deposit", u"certificate of Deposit",
                                u"need a td", u"td",u"need a Time Deposit", u"Time Deposit",
                                u"i want more information about cd",u"i want more information about td",
                                u"how much intrest of the cd ?", u"i want to know the interset of the cd ",
                                u"how much intrest of the certificate of Deposit?", u"i want to know the interset of the  certificate of Deposit",
                                u"how much intrest of the td ?", u"i want to know the interset of the td",
                                u"how much intrest of the Time Deposit?", u"i want to know the interset of the Time Deposit "],

                 u"keywords": [{u"key": u"cd", u"value": 5.0}, {u"key": u"td", u"value": 5.0}, {u"key": u"certificate of Deposit ", u"value": 5.0},
                               {u"key": u"Time Deposit", u"value": 5.0}],
                 u"keywords_ar": [
                               {u"key": u"ايه", u"value": 3.0}, {u"key": u"اية", u"value": 3.0},
                               {u"key": u"امتى", u"value": 3.0},
                               {u"key": u"ازاى", u"value": 3.0}, {u"key": u"ممكن", u"value": 3.0},
                               {u"key": u"كام", u"value": 3.0}, {u"key": u"هل", u"value": 3.0},

                              {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0},
                              {u"key": u"لدي", u"value": 3.0},{u"key": u"عندي", u"value": 4.0}, {u"key": u"عندكوا", u"value": 3.0},
                              {u"key": u"عم", u"value": 3.0},{u"key": u"لما", u"value": 3.5}, {u"key": u"مني", u"value": 3.5},
                              {u"key": u"جماعة", u"value": 4.0},{u"key": u"انتوا", u"value": 3.0}, {u"key": u"لانى", u"value": 3.0},
                              {u"key": u"كلهم", u"value": 3.5},{u"key": u"اخويا", u"value": 3.0},

                              {u"key": u"عايز", u"value": 3.5}, {u"key": u"عاوز", u"value": 3.5},
                              {u"key": u"اشترك", u"value": 4.0},{u"key": u"اعرف", u"value": 3.5}, {u"key": u"اقدم", u"value": 4.5},
                              {u"key": u"اتصلت", u"value": 4.0},{u"key": u"اعمل", u"value": 3.5}, {u"key": u"اخد", u"value": 3.0},
                              {u"key": u"تقولى", u"value": 3.0},{u"key": u"بتتحسب", u"value": 4.0},
                              {u"key": u"بتحسبوا", u"value": 4.0}, {u"key": u"متاح", u"value": 3.0},
                              {u"key": u"محتاج", u"value": 3.0}, {u"key": u"ينفع", u"value": 3.0},
                              {u"key": u"عامل", u"value": 3.0},{u"key": u"بستفسر", u"value": 3.0}, {u"key": u"كنت", u"value": 3.0},
                              {u"key": u"بسئل", u"value": 3.0},{u"key": u"سمحت", u"value": 2.0}, {u"key": u"تبقى", u"value": 3.0},
                              {u"key": u"يوجد", u"value": 4.5},{u"key": u"يساعدنى", u"value": 4.0},
                              {u"key": u"بلاقي", u"value": 3.5},{u"key": u"تساعدنى", u"value": 4.0},{u"key": u"اشترك", u"value": 4.0}, {u"key": u"بحاول", u"value": 4.0},
                              {u"key": u"طلب", u"value": 4.0},{u"key": u"اقرب", u"value": 4.5}, {u"key": u"عارف", u"value": 4.5},
                              {u"key": u"قادر", u"value": 3.5},{u"key": u"يفتح", u"value": 4.0}, {u"key": u"افتح", u"value": 4.0},
                             {u"key": u"اشتركت", u"value": 4.0}, {u"key": u"اطلب", u"value": 4.0}, {u"key": u"يساعدنى", u"value": 4.0},

                             {u"key": u"على", u"value": 4.5}, {u"key": u"قد", u"value": 3.0}, {u"key": u"لو", u"value": 2.0},
                             {u"key": u"عن", u"value": 3.0}, {u"key": u"لسه", u"value": 3.0},{u"key": u"فى", u"value": 4.5},
                             {u"key": u"الى", u"value": 3.0}, {u"key": u"عليها", u"value": 3.5},{u"key": u"دى", u"value": 3.0},

                            {u"key": u"شهادات", u"value": 5.0}, {u"key": u"ادخار", u"value": 5.0},
                            {u"key": u"إدخار", u"value": 5.0}, {u"key": u"شهادة", u"value": 5.0},
                            {u"key": u"الإدخار", u"value": 5.0},{u"key": u"الودائع لآجل", u"value": 5.0},
                            {u"key": u"ودائع", u"value": 5.0}, {u"key": u"الودائع", u"value": 5.0},
                            {u"key": u"ودائع لآجل", u"value": 5.0}, {u"key": u"اكونت", u"value": 4.0}, {u"key": u"نظام", u"value": 3.0},
                            {u"key": u"انواع", u"value": 3.5}, {u"key": u"السى اى بى", u"value": 3.0},
                            {u"key": u"فايدة", u"value": 4.5},{u"key": u"الفرع", u"value": 4.5}, {u"key": u"نسبة", u"value": 4.5},
                            {u"key": u"الورق", u"value": 4.5},{u"key": u"المطلوب", u"value": 4.5},
                            {u"key": u"الفايدة", u"value": 4.5},{u"key": u"الاجرأت", u"value": 4.5},{u"key": u"اجراء", u"value": 4.5}, {u"key": u"عاجل", u"value": 4.0},
                            {u"key": u"بنك", u"value": 4.0}, {u"key": u"الatms", u"value": 4.0},{u"key": u"atmال", u"value": 4.0},
                            {u"key": u"سى اي بى", u"value": 3.0}, {u"key": u"cib", u"value": 3.0},{u"key": u"البنك التجاري الدولي", u"value": 3.0}
                 ],
             u"answers": [u''' For more information about certificate of Deposit (CD) you can visit the following link: <br/> <a href="https://www.cibeg.com/English/Personal/Accounts/Pages/CertificateOfDeposit.aspx/" target="_blank"> https://www.cibeg.com/English/Personal/Accounts/Pages/CertificateOfDeposit.aspx</a><br/>
        			           and For more information about Time Deposit (TD) you can visit the following link: <br/> <a href="https://www.cibeg.com/English/Personal/Accounts/Pages/TimeDeposit.aspx" target="_blank"> https://www.cibeg.com/English/Personal/Accounts/Pages/TimeDeposit.aspx </a><br/>
	                           and You can register your data by visiting the following link:  <br/><a href=" http://localhost:5555/registration" target="_blank" > Registration </a> <br/>  and one of our representitives will contact you '''],

             u"answers_ar": [u''' لمعلومات اكثر عن شهادات الأدخار يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Accounts/Pages/CertificateOfDeposit.aspx/" target="_blank"> https://www.cibeg.com/arabic/Personal/Accounts/Pages/CertificateOfDeposit.aspx</a><br/>
                            ولمعلومات اكثر عن الودائع لاجل يمكنك زيارة هذا الرابط <br/> <a href="https://www.cibeg.com/arabic/Personal/Accounts/Pages/TimeDeposit.aspx/" target="_blank"> https://www.cibeg.com/arabic/Personal/Accounts/Pages/TimeDeposit.aspx/</a><br/>
                            و يمكنك ايضأ تسجيل بياناتك و سوف يقوم احد ممثلى خدمة العملاء بالتواصل معك
                            <br/><a href=" http://localhost:5555/registration_ar" target="_blank" > تسجيل </a> <br/> ''']
},

              {  u"intent": u"Have_Problems",

                      u"values": [u"I Have a Problem", u"I have Issue", u"I have an issue",u"what's the number of the call center?", u"Could you help solve my problem?",
                                  u"I need a support",u"please support me",u"how can i", u"i'm disappointed",u"error message",u"I lost my card ",
                                  u"the number of call center ",u"i want to call center", u"i want to talk call center agent",
                                  u"my card was stolen",u"i need to close account",u"Is there any problem in smart wallet"],
                      u"keywords": [{u"key": u"a issue", u"value": 5.0}, {u"key": u"problem", u"value": 5.0},{u"key": u"support", u"value": 5.0}],

                      u"keywords_ar": [{u"key": u"ايه", u"value": 3.0},{u"key": u"اية", u"value": 3.0},{u"key": u"امتى", u"value": 3.0},{u"key": u"ازاى", u"value": 3.0},
                                  {u"key": u"هل", u"value": 3.0},{u"key": u"ممكن", u"value": 3.0},{u"key": u"كام", u"value": 3.0},{u"key": u"ليه", u"value": 5.0},

                                 {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0},{u"key": u"لدي", u"value": 3.0},
                                 {u"key": u"عندي", u"value": 4.0},{u"key": u"عندكوا", u"value": 3.0},{u"key": u"انتوا", u"value": 3.0},
                                 {u"key": u"لما", u"value": 3.5},{u"key": u"مني", u"value": 3.5},{u"key": u"عم", u"value": 3.0},
                                 {u"key": u"اخويا", u"value": 3.0},{u"key": u"كلهم", u"value": 3.5}, {u"key": u"جماعة", u"value": 4.0},
                                 {u"key": u"لانى", u"value": 3.0},

                                 {u"key": u"عايز", u"value": 3.5},{u"key": u"عاوز", u"value": 3.5}, {u"key": u"اعرف", u"value": 3.5},{u"key": u"اقدم", u"value": 4.5},
                                 {u"key": u"اعمل", u"value": 3.0}, {u"key": u"اخد", u"value": 3.0}, {u"key": u"تقولى", u"value": 3.0},{u"key": u"بتتحسب", u"value": 4.0},
                                 {u"key": u"بتحسبوا", u"value": 4.0},{u"key": u"متاح", u"value": 3.0},{u"key": u"محتاج", u"value": 3.0},{u"key": u"ينفع", u"value": 3.0},
                                 {u"key": u"بستفسر", u"value": 3.0},{u"key": u"كنت", u"value": 3.0},{u"key": u"بسئل", u"value": 3.0},{u"key": u"عامل", u"value": 3.0},
                                 {u"key": u"سمحت", u"value": 2.0},{u"key": u"تبقى", u"value": 3.0},{u"key": u"يوجد", u"value": 4.5},{u"key": u"يقع", u"value": 4.0},
                                 {u"key": u"اقرب", u"value": 4.5},{u"key": u"عارف", u"value": 4.5},{u"key": u"قادر", u"value": 3.5}, {u"key": u"بلاقي", u"value": 4.5},
                                 {u"key": u"بيطلعلي", u"value": 4.5}, {u"key": u"اوقف", u"value": 5.0},{u"key": u"اغلق", u"value": 4.5},{u"key": u"اقفل", u"value": 4.5},
                                 {u"key": u"بشوف", u"value": 4.5},{u"key": u"ضاع", u"value": 5.0}, {u"key": u"اتسرق", u"value": 5.0},{u"key": u"افعل", u"value": 4.0},
                                 {u"key": u"بدوس", u"value": 4.0}, {u"key": u"بختار", u"value": 4.0}, {u"key": u"راضي", u"value": 4.0},{u"key": u"اشغل", u"value": 4.0},
                                 {u"key": u"يفتح", u"value": 4.0}, {u"key": u"افتح", u"value": 4.0},{u"key": u"اشتركت", u"value": 4.0},{u"key": u"اتصلت", u"value": 4.0},
                                 {u"key": u"برضه", u"value": 4.5},{u"key": u"احول", u"value": 3.0},{u"key": u"شغال", u"value": 4.0},{u"key": u"اوصل", u"value": 4.0},
                                 {u"key": u"مشترك", u"value": 4.0},{u"key": u"افعلها", u"value": 4.0},{u"key": u"اسجل", u"value": 3.5},{u"key": u"يقولى", u"value": 3.5},
                                 {u"key": u"بتاعي", u"value": 3.0}, {u"key": u"روح", u"value": 3.0},{u"key": u"موقفين", u"value": 4.5},{u"key": u"اكلم", u"value": 4.5},
                                 {u"key": u"عرفين", u"value": 4.0},{u"key": u"يحلوا", u"value": 4.0},{u"key": u"بدور", u"value": 4.0},{u"key": u"بقالها", u"value": 4.0},
                                 {u"key": u"مستلمتهاش", u"value": 4.0},{u"key": u"تلاقوا", u"value": 4.0},{u"key": u"شغل", u"value": 4.0},{u"key": u"شغالين", u"value": 4.0},
                                 {u"key": u"بكتب", u"value": 3.0}, {u"key": u"بقالى", u"value": 4.0}, {u"key": u"بحاول", u"value": 4.0},{u"key": u"اكلمكوا", u"value": 4.5},
                                 {u"key": u"نسيت", u"value": 5.0},{u"key": u"بتاعت", u"value": 3.0},{u"key": u"يعملوا", u"value": 3.5},{u"key": u"طلب", u"value": 4.0},
                                 {u"key": u"محدش", u"value": 4.0},{u"key": u"بيرد", u"value": 4.0},{u"key": u"اطلب", u"value": 4.0},{u"key": u"يساعدونى", u"value": 4.0},
                                 {u"key": u"يساعدنى", u"value": 4.0},{u"key": u"اشترك", u"value": 4.0},{u"key": u"فقدت", u"value": 4.0},

                                 {u"key": u"على", u"value": 4.5}, {u"key": u"قد", u"value": 3.0},{u"key": u"لو", u"value": 2.0}, {u"key": u"عن", u"value": 3.0},
                                 {u"key": u"مش", u"value": 5.0}, {u"key": u"اخر", u"value": 3.0}, {u"key": u"فى", u"value": 3.0}, {u"key": u"يا", u"value": 3.0},
                                 {u"key": u"كل", u"value": 3.0}, {u"key": u"غير", u"value": 3.0},{u"key": u"ده", u"value": 3.0}, {u"key": u"ما", u"value": 3.0},
                                 {u"key": u"الى", u"value": 3.0}, {u"key": u"عليها", u"value": 3.5},{u"key": u"دى", u"value": 3.0}, {u"key": u"لسه", u"value": 3.0},
                                 {u"key": u"اللى", u"value": 3.0},{ u"key": u"فيها", u"value": 3.0},{u"key": u"كدة",  u"value": 3.0}, { u"key": u"من",u"value": 3.5},

                                 {u"key": u"لحاجه", u"value": 4.0},{u"key": u"مره", u"value": 3.0},{u"key": u"صحيح", u"value": 3.5},{u"key": u"شهر", u"value": 4.0},
                                 {u"key": u"فضلك", u"value": 4.0},{u"key": u"مرتين", u"value": 3.0},{u"key": u"تانى", u"value": 3.5},{u"key": u"جدا", u"value": 3.0},
                                 {u"key": u"الاول", u"value": 3.5},{u"key": u"اللحظة", u"value": 3.0},{u"key": u"عطلانة", u"value": 4.5}, {u"key": u"نص", u"value": 3.5},
                                 {u"key": u"ربع", u"value": 3.5}, {u"key": u"ساعة", u"value": 4.0},{u"key": u"انتظار", u"value": 4.5},{u"key": u"رد", u"value": 4.5},
                                 {u"key": u"مرة", u"value": 3.0},{u"key": u"بايظة", u"value": 4.5},{u"key": u"طول", u"value": 3.5},

                                 {u"key": u"كارت", u"value": 4.0},{u"key": u"حساب", u"value": 3.5},
                                 {u"key": u"الكارت", u"value": 4.0},{u"key": u"الحساب", u"value": 3.5},{u"key": u"صفحة", u"value": 3.0},{u"key": u"الاكونت", u"value": 4.0},
                                 {u"key": u"رقم", u"value": 3.0},{u"key": u"مشكلة", u"value": 5.0},{u"key": u"مشكله", u"value": 5.0},{u"key": u"العملاء", u"value": 4.5},
                                 {u"key": u"خطأ", u"value": 5.0},{u"key": u"خدمة", u"value": 4.0},{u"key": u"رسالة", u"value": 3.5},{u"key": u"الموضوع", u"value": 4.0},
                                 {u"key": u"السرى", u"value": 4.0},{u"key": u"البطاقة", u"value": 4.5},{u"key": u"بطاقتى", u"value": 4.5},{u"key": u"العملا", u"value": 4.0},
                                 {u"key": u"الاسم", u"value": 4.0},{u"key": u"الباسورد", u"value": 4.0},{u"key": u"مؤقته", u"value": 4.0},{u"key": u"موجودة", u"value": 4.0},
                                 {u"key": u"الdepit card", u"value": 4.0},{u"key": u"موجود", u"value": 4.0},{u"key": u"ماكينة", u"value": 4.5},{u"key": u"الصرف", u"value": 4.5},
                                 {u"key": u"الcredit card", u"value": 4.0},{u"key": u"الatm", u"value": 4.0},{u"key": u"مدينة", u"value": 3.5},{u"key": u"حلول", u"value": 4.5},
                                 {u"key": u"مكالمة", u"value": 4.5},{u"key": u"مكالمات", u"value": 4.5},{u"key": u"credentialsال", u"value": 4.5},
                                 {u"key": u"call centerال", u"value": 4.5}, {u"key": u"حل", u"value": 4.5},{u"key": u"الماكنة", u"value": 4.5},
                                 {u"key": u"بنك", u"value": 4.0},{u"key": u"الatms", u"value": 4.0},{u"key": u"atmال", u"value": 4.0},
                                 {u"key": u"سى اي بى", u"value": 3.0}, {u"key": u"cib", u"value": 3.0},{u"key": u"البنك التجاري الدولي", u"value": 3.0}
                                 ],
                      u"answers": [u"no problem , you can call us on 19666", u"Okay, call us on 19666",u"for more details , call us on 19666"
                                   u"we can help you better if you call us on 19666", u"we hope you call us on 19666"],
                      u"answers_ar": [u"يرجى الإتصال على خدمة العملاء 19666 متاحيين 24 ساعة طوال أيام الأسبوع لمتابعة هذه الجزئية  ",
                                   u"كلمنا على 19666 وسيتم الرد عليك في أسرع وقت", u"خدمة العملاء 19666 متاحة على مدار 24 ساعة يومياً طوال أيام الأسبوع ونحن نعتذر عن التأخر في الوصول الي أحد ممثلي خدمة العملاء في بعض الأوقات وذلك نظراً لضغط المكالمات من عملاء أخرين "]
                    },
                      {
                      u"intent": u"location",
                      u"values": [u"places of atm",u"location of atms",u"branch place",u"branches location",u"i want to  go to the nearest atm",u"I want to know the nearest atm", u"i wanna know the nearest atm", u"I want to know the closest atm",u"where is the nearest atm to me? ", u"i can't find any atms in my location",u"I want to know the atms in my area",u"I want to know the locations of atms in my area?",
                                  u"i want to go to the nearest branch",u"I want to know the nearest branch",u"i wanna know the nearest branch",u"where is the nearest branch to me? ",u"I want to know the closest branch",u"I want to know the branches in my area?",u"I want to know the branches in my area",u"I want to know the locations of branches in my area"
                                  u"i want to go to the nearest bank",u"I want to know the nearest bank", u"i wanna know the nearest bank", u"I want to know the closest bank",u"where is the nearest bank to me? ", u"i can't find any bank in my location",u"I want to know the bank in my area",u"I want to know the locations of bank in my area?", u"what's the nearest bank to me ?",
                                  u"what is the nearest bank to me ?",u"what is the nearest bank to me",u"where is the nearest bank to me ?",u"where is the nearest bank to me",u"where is the closest atm ?",u"where is the closest atm"
                                  ],
                      u"keywords_ar": [{u"key": u"ايه", u"value": 3.0}, {u"key": u"امتى", u"value": 3.0}, {u"key": u"ازاى", u"value": 3.0},
                                    {u"key": u"هل", u"value": 4.0}, {u"key": u"ممكن", u"value": 3.0}, {u"key": u"كام", u"value": 3.0},
                                    {u"key": u"فين", u"value": 5.0}, {u"key": u"أين", u"value": 5.0}, {u"key": u"اين", u"value": 5.0},

                                    {u"key": u"انا", u"value": 3.0}, {u"key": u"هو", u"value": 3.0},

                                    {u"key": u"عايز", u"value": 3.5}, {u"key": u"عاوز", u"value": 3.5}, {u"key": u"اعرف", u"value": 3.5},
                                    {u"key": u"اقدم", u"value": 4.5},{u"key": u"اعمل", u"value": 3.0}, {u"key": u"اخد", u"value": 3.0},
                                    {u"key": u"تقولى", u"value": 3.0}, {u"key": u"بتتحسب", u"value": 4.0}, {u"key": u"بتحسبوا", u"value": 4.0},
                                    {u"key": u"متاح", u"value": 3.0}, {u"key": u"محتاج", u"value": 3.0}, {u"key": u"ينفع", u"value": 3.0},
                                    {u"key": u"بستفسر", u"value": 3.0}, {u"key": u"كنت", u"value": 3.0}, {u"key": u"بسئل", u"value": 3.0},
                                    {u"key": u"عامل", u"value": 3.0},{u"key": u"سمحت", u"value": 2.0}, {u"key": u"تبقى", u"value": 3.0},
                                    {u"key": u"يوجد", u"value": 4.5}, {u"key": u"يقع", u"value": 4.0}, {u"key": u"اقرب", u"value": 4.5},

                                    {u"key": u"على", u"value": 4.5}, {u"key": u"قد", u"value": 3.0}, {u"key": u"لو", u"value": 2.0},{u"key": u"او", u"value": 3.0},
                                    {u"key": u"عن",u"value": 3.0},{u"key": u"مش", u"value": 4.0},{u"key": u"فى", u"value": 4.5},{u"key": u"فضلك", u"value": 4.0},

                                    {u"key": u"اماكن", u"value": 5.0}, {u"key": u"البنك", u"value": 3.0}, {u"key": u"التجارى", u"value": 3.0},
                                    {u"key": u"الدولى", u"value": 3.0}, {u"key": u"مكان", u"value": 5.0}, {u"key": u"ماكينة", u"value": 4.5},
                                    {u"key": u"الصرف", u"value": 4.5}, {u"key": u"الفروع", u"value": 4.5}, {u"key": u"فرع", u"value": 5.0},
                                    {u"key": u"منطقة", u"value": 5.0}, {u"key": u"مناطق", u"value": 5.0}, {u"key": u"ماكنة", u"value": 4.5},
                                    {u"key": u"بنك", u"value": 4.0}, {u"key": u"الatms", u"value": 4.0}, {u"key": u"atmال", u"value": 4.5},
                                    {u"key": u"سى اي بى", u"value": 3.0},{u"key": u"cib", u"value": 3.0},{u"key": u"السى اى بى", u"value": 3.0},
                                    {u"key": u"موجودة", u"value": 4.5},{u"key": u"ماكينات", u"value": 4.5},{u"key": u"البنك التجاري الدولي", u"value": 3.0}
                                    ],
                      u"answers": [u"You can know the nearest ATMs and Branches from the following link: <a href='https://www.cibeg.com/English/Pages/branchesandatms.aspx'> https://www.cibeg.com/English/Pages/branchesandatms.aspx </a> ",
                                   u"Okay, you can visit our website to choose the nearest ATM and Branch from the following link: <a href='https://www.cibeg.com/English/Pages/branchesandatms.aspx'> https://www.cibeg.com/English/Pages/branchesandatms.aspx </a>"],
                      u"answers_ar": [u" <a href='https://www.cibeg.com/arabic/Pages/branchesandatms.aspx'> https://www.cibeg.com/arabic/Pages/branchesandatms.aspx </a>  يمكنك زيارة هذا الرابط لمعرفة جميع اماكن الفروع و ماكينات الصرف "]
                    },
                    {
                      u"intent": u"working_hours",
                      u"values": [u"I want to know the branch working hours ", u"i wanna know the openning time for ramsis branch", u"I want to know the start time of cib branches ",
                                  u"i want to know when will the branch close", u"when will the branch open and close ?"
                                  ],
                      u"keywords_ar": [{u"key": u"انا", u"value": 3}, {u"key": u"عايز", u"value": 3},{u"key": u"عاوز", u"value": 3},
                                       {u"key": u"اعرف", u"value": 3.5},{u"key": u"بيفتح", u"value": 5.0}, {u"key": u"بتفتح", u"value": 5.0},
                                       {u"key": u"البنك", u"value": 4.0},{u"key": u"التجارى", u"value": 3.0},
                                       {u"key": u"الدولى", u"value": 3.0},{u"key": u"أين", u"value": 4.0},{u"key": u"متى", u"value": 5.0},
                                       {u"key": u"امتى", u"value": 5.0},{u"key": u"بيقفل", u"value": 5.0}, {u"key": u"الفرع", u"value": 4.5},
                                       {u"key": u"الفروع", u"value": 4.5},{u"key": u"مواعيد", u"value": 5.0}, {u"key": u"العمل", u"value": 4.5},
                                       {u"key": u"تقولى", u"value": 3.0},{u"key": u"ممكن", u"value": 3.0},{u"key": u"لو", u"value": 2.0},
                                       {u"key": u"سمحت", u"value": 2.0}, {u"key": u"بستفسر", u"value": 3.0},{u"key": u"عن", u"value": 3.0},
                                       {u"key": u"اوقات", u"value": 5.0}, {u"key": u"فاتح", u"value": 4.0},{u"key": u"لحد", u"value": 3.5},
                                       {u"key": u"الساعة", u"value": 5.0},{u"key": u"كام", u"value": 3.5},{u"key": u"البنك التجاري الدولي", u"value": 3.0}
                                      ],
                      u"answers": [u"You can know the Branches working hours from the following link: <a href='https://www.cibeg.com/English/Pages/branchesandatms.aspx'> https://www.cibeg.com/English/Pages/branchesandatms.aspx </a> ",
                                   u"Okay, you can visit our website to know the branches working hours from the following link: <a href='https://www.cibeg.com/English/Pages/branchesandatms.aspx'> https://www.cibeg.com/English/Pages/branchesandatms.aspx </a>"],
                      u"answers_ar": [u" <a href='https://www.cibeg.com/arabic/Pages/branchesandatms.aspx'> https://www.cibeg.com/arabic/Pages/branchesandatms.aspx </a>  يمكنك زيارة هذا الرابط لمعرفة اوقات عمل الفروع"]
                    }



]

# Get maximum similarity from list items
#def get_intent_similarity(intent, question):
#    similarity = []
#    qust = nlp(question)

#    for i in intent:
#        doc = nlp(i)
#        similarity.append(qust.similarity(doc))

#    similarity = sorted(similarity, reverse=True)
#    return similarity[0]


def get_all_similarity(question):
    results = []
    similarity = []

    qust = nlp(question.lower())

    for intent in bag_of_intents:
        similarity = []

        print(intent[u"intent"] + " is arabic: " + str(is_arabic(question)))

        if not is_arabic(question):
            for i in intent[u"values"]:
                doc = nlp(i)
                similarity.append(qust.similarity(doc))
        else:
            matched = 0.0
            for i in intent[u"keywords_ar"]:
                for j in question.split():
                    if j == i[u"key"]:
                        matched += i[u"value"]

            if matched >= 0:
                print("Equation Before : " + str(float(matched)/float(len(question.split()))))
                similarity.append(float(matched)/float(len(question.split())))
                similarity.append(float(matched)/float(len(question.split())))
                print("Equation After : " + str(similarity))
            else:
                similarity.append(0.0)
                similarity.append(0.0)


        # explicit keyword mention means more weight to the intent
        if u"keywords" in intent:
            for i in intent[u"keywords"]:
                if question.lower().find(i[u"key"]) >= 0:
                    similarity = [s * i[u"value"] for s in similarity]
                    print("keywords: " + str(similarity))
                    break

        # if question is not english decrease weights of similarity
        if detect(question) != u"en" and not is_arabic(question):
            similarity = [s * 0.7 for s in similarity]
            print("detect(question): " + str(similarity))

        #if is_arabic(question):
        #    similarity = [s * 1.2 for s in similarity]
        #    print("is_arabic(question): " + str(similarity))

        similarity = sorted(similarity, reverse=True)
        print("sorted: " + str(similarity))
        results.append({ u"intent": intent[u"intent"], u"value": (similarity[0] + similarity[1]) / 2.0 })

    results = sorted(results, key=operator.itemgetter(u"value"), reverse=True)
    return results

def is_arabic(phrase):
    for i in arabic_letters:
        if phrase.find(i) > 0:
            return True
    return False