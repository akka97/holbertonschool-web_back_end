export default function cleanSet(set, startString) {
  // Check if set is a Set
  if (!(set instanceof Set)) {
    throw new Error('The first argument must be a Set.');
  }

  // Check if startString is a non-empty string
  if (typeof startString !== 'string' || startString === '') {
    throw new Error('The second argument must be a non-empty string.');
  }

  const arr = [];

  set.forEach((element) => {
    // Check if element is defined and starts with startString
    if (element !== undefined && element.startsWith(startString)) {
      arr.push(element.substring(startString.length));
    }
  });

  return arr.join('-');
}
