import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { DEFAULTUSER, User } from '../models/user.model';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { ClassGroup, DEFAULTCLASS } from '../models/class.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  users = new Subject<User[]>();

  currentUser = DEFAULTUSER;

  currentClass = DEFAULTCLASS
  
  
  constructor(public http:HttpClient) { }

  fetchClass() {
    this.http.get<ClassGroup>(environment.url + 'class').subscribe(
      (data) => {
        this.currentClass = data;
      },
      (error) => console.log(error)
    );
  }

  getClass() {
    return this.currentClass
  }

  getStudents(){
    return this.users.asObservable();
  }
  
  fetchStudents(){
    this.http.get<User[]>(environment.url + 'students').subscribe(
      (data) => {
        this.users.next(data);
      },
      (error) => console.log(error)
    );
  }

  addCollegeStudent(classID:number, studentID:number) {
    this.http.post(environment.url + 'student', {}).subscribe(
      () => {},
      (error) => console.log(error)
    );
  }

  setCurrnetUser(email:string, password:string){
    this.http.get<User>(environment.url+"user").subscribe((data)=>{
      this.currentUser = data;
    },
    error=>console.log(error)
    )
  }

  getCurrentUser(){
    if(this.currentUser.email=''){
      throw Error;
    }
    else
      return this.currentUser
  }

  registerUser(email:string, password:string, roleID:number){
    this.http
      .post(environment.url + 'user', {
        email: email,
        password: password,
        role: roleID,
      })
      .subscribe(
        () => {},
        (error) => console.log(error)
      );
  }

}
