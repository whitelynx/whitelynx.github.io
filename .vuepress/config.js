const fs = require('fs');


const defaultThemeConfig = {
  email: '',
  address1: '',
  address2: '',
  city: '',
  state: '',
  zip: '',
  country: '',
  url: 'https://whitelynx.github.io',
  phoneNumber: '',
  confirm: true,
  stateAbbr: '',
  addressQuery: '',
  showContactInfo: false
};

let themeConfig = defaultThemeConfig;
try {
    themeConfig = JSON.parse(fs.readFileSync('.last-gulp-answers.json'));
} catch(exc) {
    console.warn('Exception reading .last-gulp-answers.json; using default theme config.', exc);
}


module.exports = {
    title: 'David H. Bronke',
    description: 'Software architect/engineer',
    themeConfig,
    extendMarkdown(md) {
        md.use(require('markdown-it-deflist'));
    }
};
