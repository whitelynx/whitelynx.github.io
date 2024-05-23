import fs from 'fs';

import { viteBundler } from '@vuepress/bundler-vite';
import { whitelynxTheme } from './theme';
import { defineUserConfig } from 'vuepress';

import markdownItDeflist from 'markdown-it-deflist';


const defaultThemeData = {
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

let themeData = defaultThemeData;
try {
    themeData = JSON.parse(fs.readFileSync('.last-gulp-answers.json'));
} catch(exc) {
    console.warn('Exception reading .last-gulp-answers.json; using default theme config.', exc);
}


export default defineUserConfig({
    title: 'David H. Bronke',
    description: 'Software architect/engineer',
    theme: whitelynxTheme(themeData),
    bundler: viteBundler(),
    extendsMarkdown: (md) => {
        md.use(markdownItDeflist);
    },
});
