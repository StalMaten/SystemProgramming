<?php
class Employee
{
    public $name;
    public $age;
    public $salary;

    public function getName(){
        return $this->name . "\n";
    }

    public function getAge(){
        return $this->age . "\n";
    }

    public function getSalary(){
        return $this->salary . "\n";
    }

    public function checkAge(){
        return $this->age>18;
    }
}

$eric=new Employee;
$eric->name='Eric';
$eric->age=25;
$eric->salary=10000;
echo $eric->getName();
echo $eric->getAge();
echo $eric->getSalary();
echo $eric->checkAge();

$john=new Employee;
$john->name='John';
$john->age=17;
$john->salary=6000;

echo $eric->getSalary() + $john->getSalary();
