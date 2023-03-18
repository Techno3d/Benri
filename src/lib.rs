use std::{fs::{self, File}, path::Path, io::Write};

use directories::BaseDirs;
use pyo3::prelude::*;
use serde::{Deserialize, Serialize};

#[pyfunction]
fn setup() -> Vec<Data> {
    if let Some(base_dirs) = BaseDirs::new() {
        let data_dir = base_dirs.data_dir();
        let data = data_dir.to_str().unwrap().to_owned() + "/benri/";
        let path = Path::new(&data);
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
                let contents = serde_json::to_vec(&vec![Data::default()]).unwrap();
                let mut file = File::create(Path::new(&(main_folder + "Tasks.json"))).unwrap();
                file.write_all(&contents).unwrap();
                file.sync_all().unwrap();
                return vec![Data::default()];
            },
        };
        return serde_json::from_str::<Vec<Data>>(&fs::read_to_string(main_file).unwrap()).unwrap();
    }
    return vec![Data::default()];
}

#[pyfunction]
fn get_tasks() -> Vec<Data> {
    if let Some(base_dirs) = BaseDirs::new() {
        let data_dir = base_dirs.data_dir();
        let data = data_dir.to_str().unwrap().to_owned() + "/benri/Tasks.json";
        let main_file = Path::new(&data);
        return serde_json::from_str::<Vec<Data>>(&fs::read_to_string(main_file).unwrap()).unwrap();
    }
    return vec![Data::default()];
}

#[pyfunction]
fn add_task(name: String, completed: bool, link: Option<String>) {
    if let Some(base_dirs) = BaseDirs::new() {
        let data_dir = base_dirs.data_dir();
        let data = data_dir.to_str().unwrap().to_owned() + "/benri/Tasks.json";
        let main_file = Path::new(&data);
        let mut tasks = get_tasks();
        tasks.push(Data {name, completed, link});

        fs::write(main_file, serde_json::to_vec(&tasks).unwrap()).unwrap();
    }
}

#[pyfunction]
fn set_tasks(tasks: Vec<(String, bool, Option<String>)>) {
    let tasks: Vec<Data> = tasks.iter().map(|x| Data {name: x.0.clone(), completed: x.1, link: x.2.clone()}).collect();
    if let Some(base_dirs) = BaseDirs::new() {
        let data_dir = base_dirs.data_dir();
        let data = data_dir.to_str().unwrap().to_owned() + "/benri/Tasks.json";
        let main_file = Path::new(&data);

        fs::write(main_file, serde_json::to_vec(&tasks).unwrap()).unwrap();
    }
}

#[derive(Default, Deserialize, Serialize, Debug)]
#[pyclass]
struct Data {
    #[pyo3(get, set)]
    name: String,
    #[pyo3(get, set)]
    completed: bool,
    #[pyo3(get, set)]
    link: Option<String>,
}

#[pymethods]
impl Data {
    #[new]
    fn new(name: String, completed: bool, link: Option<String>) -> PyResult<Self> {
        Ok(Data {name, completed, link })
    }
    fn destructure(&self) -> (String, bool, Option<String>) {
        (self.name.clone(), self.completed, self.link.clone())
    }
}

#[pymodule]
fn benri_api(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(setup, m)?)?;
    m.add_function(wrap_pyfunction!(get_tasks, m)?)?;
    m.add_function(wrap_pyfunction!(add_task, m)?)?;
    m.add_function(wrap_pyfunction!(set_tasks, m)?)?;
    m.add_class::<Data>()?;
    Ok(())
}
