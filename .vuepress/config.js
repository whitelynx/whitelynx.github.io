const fs = require('fs');


module.exports = {
    title: 'David H. Bronke',
    description: 'Software architect/engineer',
    themeConfig: JSON.parse(fs.readFileSync('.last-gulp-answers.json')),
    markdown: {
        config: md => {
            md.use(require('markdown-it-deflist'));
        }
    }
};
