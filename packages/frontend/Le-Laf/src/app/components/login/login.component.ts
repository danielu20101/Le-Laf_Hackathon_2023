import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ModalService } from 'src/app/services/modal.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email:string="";
  password:string="";

constructor(public router:Router,public modalService:ModalService) {}

login(){
  this.modalService.logIn();
  this.router.navigate(['/home']);
}
register(){
  this.router.navigate(['/register']);
}
}
