import { API_URLS } from './../../shared/utilities/service-config';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ChatBotService {
  public currentMessages = [{
    text: 'Hello, Welcome to CIB bank chat bot! I can speak in English and Arabic',
    byMe: false
  }];

  constructor(private httpClinet: HttpClient) { }

  questionProcess(question: string) {
    this.currentMessages.push({
      text: question,
      byMe: true
    });
    return this.httpClinet.post(API_URLS.PROCESS_QUESTION(question), '').pipe(
      tap((res: any) => {
          this.currentMessages.push({
            text: res.answer,
            byMe: false
          });
      })
    );
  }
}
