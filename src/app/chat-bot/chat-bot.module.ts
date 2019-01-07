import { MessageItemComponent } from './components/message-item/message-item.component';
import { ChatBotRoutingModule } from './chat-bot-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChatViewComponent } from './views/chat-view/chat-view.component';
import { SharedModule } from '@app/shared/shared.module';
import { RegistrationComponent } from './views/registration/registration.component';
import { HirarchyComponent } from './views/employees/hirarchy/hirarchy.component';

@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    ChatBotRoutingModule
  ],
  declarations: [ChatViewComponent, MessageItemComponent, RegistrationComponent, HirarchyComponent]

})
export class ChatBotModule { }
