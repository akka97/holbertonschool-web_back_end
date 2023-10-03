export default function divideFunction(numerator, deminator) {
    if (deminator === 0) {
        throw new Error('cannot devide by 0');
    } else {
        return numerator/deminator
    }
}
