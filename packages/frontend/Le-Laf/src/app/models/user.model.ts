export type User = {
    userID:number;
    email:string;
    password:string;
    roleID:number;
}

export var DEFAULTUSER:User = {
    userID:-1,
    email:'',
    password:'',
    roleID:0
} 