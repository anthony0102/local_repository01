<?php
     header('Content-Type: application/json');
      header('Content-Type: text/html;charset=utf-8');
    header('Access-Control-Allow-Origin:*');
    header('Access-Control-Allow-Methods:*');
    header('Access-Control-Allow-Headers:x-requested-with,content-type');

    echo file_get_contents('tabledata.json');