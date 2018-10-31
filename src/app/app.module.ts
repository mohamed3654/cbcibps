import { AppRoutingModule } from './app-routing.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from '@app/app.component';
import { MainHeaderComponent } from '@app/layout/components/main-header/main-header.component';
import { MainFooterComponent } from '@app/layout/components/main-footer/main-footer.component';
import { NotFoundComponent } from '@app/layout/views/not-found/not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    MainHeaderComponent,
    MainFooterComponent,
    NotFoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
