import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DateExtrasService {

  public url = 'http://127.0.0.1:5000/all';
  constructor(
    public http:HttpClient
  ) { }

  public getData() : Observable<any> {
    return this.http.get(`${this.url}`);
  }
  
}
