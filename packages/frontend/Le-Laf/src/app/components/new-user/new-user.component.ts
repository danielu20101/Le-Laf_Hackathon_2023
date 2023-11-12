import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { ModalService } from 'src/app/services/modal.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-new-user',
  templateUrl: './new-user.component.html',
  styleUrls: ['./new-user.component.css']
})
export class NewUserComponent {
  email:string="";
  password:string="";

  selectedRole:{name:string,id:number}|undefined=undefined;
  roles:{name:string,id:number}[] = [
    {name:'College Student',id:0},
    {name:'College Admin',id:1},
    {name:'High School Admin',id:2}
  ]



  constructor(public modalService:ModalService, public router:Router, public userService:UserService,public messageService:MessageService){}

  login() {
        ///Create User
    if (this.selectedRole == undefined){
      this.messageService.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Please Select a Role',
      });
      return;
    }
    
    this.userService
      .registerUser(this.email, this.password, this.selectedRole.id)
      .subscribe(
        () => {
          this.modalService.logIn();
          this.router.navigate(['/home']);
        },
        (error) =>
          this.messageService.add({
            severity: 'error',
            summary: 'Error',
            detail: 'Invalid Credentials',
          })
      );
  }

  back() {
    this.router.navigate([''])
  }
}
