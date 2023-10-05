export default function getListStudentsIds (arrayOfObjects) {
    if (!Array.isArray(arrayOfObjects)) {
        return [];
    }
    return arrayOfObjects.map((student) => student.id)
}
