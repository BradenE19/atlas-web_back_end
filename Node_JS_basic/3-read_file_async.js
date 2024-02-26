const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const students = data.trim().split('\n').slice(1).map(line => line.split(','));
        const fields = {};
        students.forEach(student => {
          for (let i = 0; i < student.length - 1; i++) {
            if (!fields[student[i]]) {
              fields[student[i]] = [];
            }
            fields[student[i]].push(student[0]);
          }
        });

        const totalCount = students.length;
        console.log(`Number of students: ${totalCount}`);

        Object.entries(fields).forEach(([field, students]) => {
          console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        });

        resolve(totalCount);
      }
    });
  });
}

module.exports = countStudents;
