<?php
class Path
{
    public $current_path;

    function __construct($path)
    {
        $this->current_path = (file_exists ( $path)) ? $path : die('Invalid Path');
    }

    public function cd($new_path)
    {
            //splice current_path
            $current_folders = explode('/', $this->current_path);

            //splice new path
            if (preg_match('/^[a-zA-Z\/\.]+$/', $new_path)){
                $new_folders = (explode('/', $new_path));
            } else {
                die('Invalid path, use alphabet letters only!');
            }

            //add new path to current_path
            foreach($new_folders as $key=>$folder){

                switch ($folder) {
                    case "..":
                        array_pop($current_folders);
                        break;
                    case "."://do nothing 
                        break;
                    case "":
                        $current_folders = array('');
                        break;
                    case (preg_match('/^[a-zA-Z]+$/', $folder) == true) :
                        array_push($current_folders, $folder);
                        break;                        
                    default:
                        break;
                }

                // print_r($current_folders);

            }

            var_dump(implode('/',$current_folders));

    }

}

$path = new Path('/home/user/public_html/everli');
echo $path->current_path;
$path->cd('/');
$path->cd('../x');
$path->cd('./x');
$path->cd('x');
$path->cd('/a');
$path->cd('../../e/../f');
$path->cd('/d/e/../a');
$path->cd('d/e/../a');
