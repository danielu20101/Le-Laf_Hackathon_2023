import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { DEFAULTUSER, User } from '../models/user.model';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { ClassGroup, DEFAULTCLASS } from '../models/class.model';
import { HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  users = new Subject<User[]>();

  currentUser = DEFAULTUSER;

  currentClass = DEFAULTCLASS
  
  
  constructor(public http:HttpClient) { }

  fetchClass(profID:number) {
         const options = profID
           ? {
               params: new HttpParams()
                 .set('profID', profID)
             }
           : {};

   return this.http.get<ClassGroup>(environment.url + 'getClass',options);
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

  setCurrentUser(email:string, password:string){
     const options = email ? { params: new HttpParams().set('email', email).append('password',password) } : {};
    return this.http.get<User>(environment.url+"getUser",options)
    
  }

  getCurrentUser(){
    if(this.currentUser.email=''){
      throw Error;
    }
    else
      return this.currentUser
  }

  registerUser(email:string, password:string, roleID:number){
    return this.http
      .post(environment.url + 'registerUser', {
        'email': email,
        'password': password,
        'role': roleID,
      })
      
  }

}
