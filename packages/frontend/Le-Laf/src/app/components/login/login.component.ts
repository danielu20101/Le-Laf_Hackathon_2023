import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { ModalService } from 'src/app/services/modal.service';
import { UserService } from 'src/app/services/user.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email:string="";
  password:string="";

constructor(public router:Router,public modalService:ModalService,public userService:UserService, public messageService:MessageService) {}

login(){
  this.userService.setCurrentUser(this.email,this.password).subscribe((data)=>{
    this.userService.currentUser = data
    this.modalService.logIn();
    this.router.navigate(['/home']);
  },error=>this.messageService.add({severity:'error',summary:'Error',detail:'Invalid Login'}))

}

register(){
  this.router.navigate(['/register']);
}
}
