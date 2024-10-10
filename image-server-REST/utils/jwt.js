const expressJwt = require('express-jwt');
const config = require('config.json');

module.exports = jwt;

function jwt() {
    const secret = config.secret;
    return expressJwt({ secret, algorithms: ['HS256'] }).unless({
        path: [
            // No auth required for these APIs
            '/',
            '/login',
            '/signup',
            '/starter-page',
            '/frontend',
            '/health',
            '/users/register',
            '/users/login',
            '/images/getSelected',
            // Use a RegExp to match any route under /images/i/<imageId>
            /^\/images\/i\/.+$/
        ]
    });
}