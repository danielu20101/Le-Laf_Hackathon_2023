import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { ClassComponent } from './components/class/class.component';
import { AcceptComponent } from './components/accept/accept.component';
import { RequestComponent } from './components/request/request.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: '', component: LoginComponent },
  { path: 'class', component: ClassComponent },
  { path: 'accept', component: AcceptComponent },
  { path: 'request', component: RequestComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
