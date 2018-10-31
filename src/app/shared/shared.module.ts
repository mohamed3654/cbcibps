import { ChatBotService } from './../chat-bot/service/chat-bot.service';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    HttpModule,
    HttpClientModule
  ],
  declarations: [],
  providers: [ChatBotService],
  exports: [
    FormsModule,
    HttpModule,
    HttpClientModule
  ]
})
export class SharedModule { }
