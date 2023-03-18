use std::{fs::{self, File}, path::Path, io::Write};

use directories::BaseDirs;
use serde::{Deserialize, Serialize};

fn main() {
    if let Some(base_dirs) = BaseDirs::new() {
        let data_dir = base_dirs.data_dir();
        let data = data_dir.to_str().unwrap().to_owned() + "/benri/";
        let path = Path::new(&data);
        println!("{:?}", path);
        let main_folder = match path.try_exists() {
            Ok(true) => data.clone(),
            _ => {
                fs::create_dir(data.clone()).unwrap();
                data.clone()
            },
        };
        
        let main_file = match Path::new(&(main_folder.clone() + "Tasks.json")).try_exists() {
            Ok(true) => data + "Tasks.json",
            _ => {
                let contents = serde_json::to_vec(&vec![Task::default()]).unwrap();
                let mut file = File::create(Path::new(&(main_folder + "Tasks.json"))).unwrap();
                file.write_all(&contents).unwrap();
                file.sync_all().unwrap();
                println!("{:?}", vec![Task::default()]);
                return;
            },
        };
        println!("{:?}", serde_json::from_str::<Vec<Task>>(&fs::read_to_string(main_file).unwrap()).unwrap());
    }
}

#[derive(Default, Deserialize, Serialize, Debug)]
struct Task {
    name: String,
    completed: bool,
    link: Option<String>,
}
