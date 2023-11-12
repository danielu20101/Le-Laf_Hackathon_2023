import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ModalService } from 'src/app/services/modal.service';

@Component({
  selector: 'menubar',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent {
  items = [
    {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      routerLink: '/home',
    },
    {
      label: 'View Class',
      icon: 'pi pi-fw pi-users',
      routerLink: '/class',
    },
    {
      label: 'View Pending Requests',
      icon: 'pi pi-fw pi-calendar-minus',
      routerLink: '/accept',
    },
    {
      label: 'Request Event',
      icon: 'pi pi-fw pi-calendar-plus',
      routerLink: '/request',
    },
  ];

  constructor(public router:Router, public modalService:ModalService) {}

  logout() {
    this.modalService.logOut();
    this.router.navigate(['']);
  }
}
