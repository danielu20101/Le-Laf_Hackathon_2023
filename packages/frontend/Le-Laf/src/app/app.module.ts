import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { ClassComponent } from './components/class/class.component';
import { RequestComponent } from './components/request/request.component';
import { AcceptComponent } from './components/accept/accept.component';
import { MenuComponent } from './components/menu/menu.component';
import { MenubarModule } from 'primeng/menubar';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { TableModule } from 'primeng/table';
import { RegisterComponent } from './components/register/register.component';
import { DialogModule } from 'primeng/dialog';


@NgModule({
  declarations: [AppComponent, HomeComponent, LoginComponent, ClassComponent, RequestComponent, AcceptComponent, MenuComponent, RegisterComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory,
    }),
    MenubarModule,
    ButtonModule,
    CardModule,
    TableModule,
    DialogModule
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
