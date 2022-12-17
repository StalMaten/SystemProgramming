<?php
class User
{
    public $name;
    public $age;

    public static function show($str){
        echo $str . "!";
    }
}

$user=new User;
$user->name='John';
$user->age=24;

$user->show('Hello World');
