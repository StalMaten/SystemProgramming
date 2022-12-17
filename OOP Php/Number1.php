<?php
class Employee
{
    public $name;
    public $age;
    public $salary;

}

$john=new Employee;
$john->name='john';
$john->age=25;
$john->salary=1000;

$eric=new Employee;
$eric->name=26;
$eric->age=26;
$eric->salary=2000;

echo ($john->salary + $eric->salary . "\n");
echo ($john->age + $eric->age);
