import { Component } from '@angular/core';
import { ModalService } from 'src/app/services/modal.service';

@Component({
  selector: 'app-class',
  templateUrl: './class.component.html',
  styleUrls: ['./class.component.css']
})
export class ClassComponent {
  classTime = "10:00 AM - 11:00 AM";
  classDay = "Monday";
  members = [
    {
      id:1,
      name: "Paolo",
    }
  ]
  showing_register = false;

  
  constructor(public modalService: ModalService) { }

  ngOnInit(): void {
    this.modalService.addingMembersObservable().subscribe((status)=>{
      this.showing_register = status;
    })
  }
  
  showRegister() {
    this.showing_register = true;
    this.modalService.showAddMembers();
  }

}
