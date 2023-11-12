import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ModalService {

  adding_members = new Subject<boolean>();

  logged_in = new Subject<boolean>();

  constructor() { }

  hideAddMembers() {
    this.adding_members.next(false);
  }

  showAddMembers() {
    this.adding_members.next(true);
  }

  addingMembersObservable() {
    return this.adding_members.asObservable();
  }

  logOut(){
    this.logged_in.next(false);
  }

  logIn(){
    this.logged_in.next(true);
  }

  loggedInObservable(){
    return this.logged_in.asObservable();
  }

}
