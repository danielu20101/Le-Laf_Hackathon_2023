import { Component } from '@angular/core';
import { ModalService } from 'src/app/services/modal.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent {
  members = [
    {
      id: 2,
      name: 'Joe',
    },
    {
      id: 3,
      name: 'Dan',
    },
  ];
  selectedMembers = [];
  constructor(public modalService: ModalService) {}

  close() {
    this.modalService.hideAddMembers();
  }

  save() {
    /////
    this.close();
  }
}
