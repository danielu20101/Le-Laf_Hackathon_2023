import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { RequestedEvent } from '../models/request.model';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RequestService {
  requests = new Subject<RequestedEvent[]>();

  constructor(public http:HttpClient) { }

  fetchRequests(userID:number){
    this.http.get<RequestedEvent[]>(environment.url+"requested").subscribe((data)=>{
      this.requests.next(data);
    },
    error=>console.log(error))
  }

  getRequsts(){
    return this.requests.asObservable();
  }

}
