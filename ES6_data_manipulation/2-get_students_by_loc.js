export default function getListStudentsByLocation(listOfStudent, city) {
    return listOfStudent.filter((cities) => cities.location === city);
}
