export default function getListStudentsIds () {
    if (!Array.isArray(arrayOfObjects)) {
        return [];
    }
    return arrayOfObjects.map((student) => student.id)
}
