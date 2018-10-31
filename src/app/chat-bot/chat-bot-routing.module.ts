import { ChatViewComponent } from './views/chat-view/chat-view.component';
import { routesConfig } from '@app/shared/utilities/pages-config';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '', redirectTo: routesConfig.chatBot.chat.name , pathMatch: 'full'
      },
      {
        path: routesConfig.chatBot.chat.name,
        component: ChatViewComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ChatBotRoutingModule { }
