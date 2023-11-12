import { User } from "./user.model"

export type ClassGroup = {
    classID:number,
    profID:number,
    users:User[],
    dayCode:number,
    startTime:string,
    endTime:string
}

export var DEFAULTCLASS:ClassGroup = {
    classID:0,
    profID:0,
    users:[],
    dayCode:0,
    startTime:'',
    endTime:''
}