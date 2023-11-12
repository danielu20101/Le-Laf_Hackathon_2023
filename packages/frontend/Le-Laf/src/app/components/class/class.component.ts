import { Component } from '@angular/core';
import { ClassGroup, DEFAULTCLASS } from 'src/app/models/class.model';
import { User } from 'src/app/models/user.model';
import { ModalService } from 'src/app/services/modal.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-class',
  templateUrl: './class.component.html',
  styleUrls: ['./class.component.css']
})
export class ClassComponent {
  classTime = "10:00 AM - 11:00 AM";
  classDay = "Monday";
  members:User[] = []
  showing_register = false;
  currentClass:ClassGroup=DEFAULTCLASS;
  
  constructor(public modalService: ModalService,public userService:UserService) { }

  ngOnInit(): void {
    this.modalService.addingMembersObservable().subscribe((status)=>{
      this.showing_register = status;
    })
    
    this.userService.fetchClass(this.userService.getCurrentUser().role).subscribe((data)=>{
      this.currentClass = data;
      this.members = this.currentClass.users
    })
  }
  
  showRegister() {
    this.showing_register = true;
    this.modalService.showAddMembers();
  }

}
