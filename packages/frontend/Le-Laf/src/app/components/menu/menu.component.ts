import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DEFAULTUSER } from 'src/app/models/user.model';
import { ModalService } from 'src/app/services/modal.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'menubar',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent implements OnInit{
  items = [
    {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      routerLink: '/home',
    },
  ];



  constructor(public router:Router, public modalService:ModalService, public userService:UserService) {}

  ngOnInit(): void {
    var curr_user = this.userService.getCurrentUser()
    if (curr_user==DEFAULTUSER){
      this.router.navigate([''])
    }
     const roleID =  curr_user.role

     if(roleID==0)
      return
     else if (roleID==1){
      this.items.push({
      label: 'View Class',
      icon: 'pi pi-fw pi-users',
      routerLink: '/class',
    },
    {
      label: 'View Pending Requests',
      icon: 'pi pi-fw pi-calendar-minus',
      routerLink: '/accept',
    })
     }
    else {
      this.items.push({
        label: 'Request Event',
        icon: 'pi pi-fw pi-calendar-plus',
        routerLink: '/request',
      });
    }
  }

  logout() {
    this.modalService.logOut();
    this.router.navigate(['']);
  }
}   