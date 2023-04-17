<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token');

// get the data from the POST message
$post_data = json_decode(file_get_contents('php://input'), true);
$data = $post_data['filedata'];
// generate a unique ID for the file, e.g., session-6feu833950202
$file = uniqid("session-");
// the directory "data" must be writable by the server
$name = "newDataVerbTense/{$file}.csv";
// write the file to disk
//if statement prevents odd bug where empty duplicate files were sent to the data directory
if (strlen($data) >0) {
    file_put_contents($name, $data);
}
?>