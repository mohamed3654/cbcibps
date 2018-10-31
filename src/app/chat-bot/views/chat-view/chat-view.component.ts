import { ChatBotService } from './../../service/chat-bot.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chat-view',
  templateUrl: './chat-view.component.html',
  styleUrls: ['./chat-view.component.scss']
})
export class ChatViewComponent {

  public message = {text: ''};

  public pendingRequest = false;

  public mostFrequent = [
    'I want to know the branch working hours',
    'when will the branch open and close ?',
    'I Have a Problem',
    'I want to take loan'
  ];

  constructor(private chatBotService: ChatBotService) { }

  get messages() {
    return this.chatBotService.currentMessages;
  }

  sendMessage(question: string) {
    if (question || this.message.text) {
      this.pendingRequest = true;
      this.chatBotService.questionProcess(question || this.message.text)
      .subscribe(() => this.pendingRequest = false, () => this.pendingRequest = false);
      this.message = {text: ''};
    }
  }

}
