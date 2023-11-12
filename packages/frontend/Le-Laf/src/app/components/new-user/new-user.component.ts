import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ModalService } from 'src/app/services/modal.service';

@Component({
  selector: 'app-new-user',
  templateUrl: './new-user.component.html',
  styleUrls: ['./new-user.component.css']
})
export class NewUserComponent {
  email:string="";
  password:string="";

  selectedRole:string="";
  roles = [
    {name:'College Admin'},
    {name:'College Student'},
    {name:'High School Admin'}
  ]



  constructor(public modalService:ModalService, public router:Router){}

  login() {
        ///Create User
    this.modalService.logIn()
    this.router.navigate(['/home'])
  }

  back() {
    this.router.navigate([''])
  }
}
