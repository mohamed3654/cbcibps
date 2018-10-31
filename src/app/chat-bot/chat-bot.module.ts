import { MessageItemComponent } from './components/message-item/message-item.component';
import { ChatBotRoutingModule } from './chat-bot-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChatViewComponent } from './views/chat-view/chat-view.component';
import { SharedModule } from '@app/shared/shared.module';

@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    ChatBotRoutingModule
  ],
  declarations: [ChatViewComponent, MessageItemComponent]

})
export class ChatBotModule { }
