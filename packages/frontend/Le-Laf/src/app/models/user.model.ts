export type User = {
    userID:number;
    email:string;
    password:string;
    roleID:number;
}

export var DEFAULTUSER:User = {
    userID:0,
    email:'',
    password:'',
    roleID:0
} 