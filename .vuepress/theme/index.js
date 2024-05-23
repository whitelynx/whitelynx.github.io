import { getDirname, path } from 'vuepress/utils';
import { themeDataPlugin } from '@vuepress/plugin-theme-data';

const __dirname = getDirname(import.meta.url);

export const whitelynxTheme = (options) => {
    return {
        name: 'vuepress-theme-whitelynx',

        // path to the client config of your theme
        clientConfigFile: path.resolve(__dirname, 'client.js'),

        // set custom dev / build template
        // if the template is not specified, the default template
        templateBuild: path.resolve(__dirname, 'templates/build.html'),
        templateDev: path.resolve(__dirname, 'templates/dev.html'),

        // use plugins
        plugins: [
            themeDataPlugin(options),
        ],

        // other plugin APIs are also available
    }
};
