import { NotFoundComponent } from './layout/views/not-found/not-found.component';
import { routesConfig } from './shared/utilities/pages-config';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';


@NgModule({
  imports: [
    RouterModule.forRoot([
      {
        path: '',
        redirectTo: routesConfig.chatBot.name,
        pathMatch: 'full'
      },
      {
        path: routesConfig.chatBot.name,
        loadChildren: routesConfig.chatBot.module,
      },
      {
        path: '**',
        component: NotFoundComponent
      }
    ], { useHash: false, onSameUrlNavigation: 'reload' })
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {
}

