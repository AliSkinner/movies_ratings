var gulp = require('gulp'),
    cssnano = require('gulp-cssnano'),
    uglify = require('gulp-uglify'),
    del = require('del'),
    less = require('gulp-less'),
    path = require('path'),
    sourcemaps = require('gulp-sourcemaps');

// build less
gulp.task('less', function () {
  return gulp.src('movies_ratings/assets/stylesheets/less/*.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less') ]
    }))
    .pipe(cssnano())
    .pipe(gulp.dest('movies_ratings/assets/stylesheets/css'))
});

// build js
gulp.task('scripts', function() {
  return gulp.src('movies_ratings/assets/js/src/*.js')
    .pipe(sourcemaps.init())
      .pipe(uglify())
      .pipe(sourcemaps.write('/'))
    .pipe(gulp.dest('movies_ratings/assets/js/scripts'))
});

// clean js & css dirs
gulp.task('clean', function() {
  return del([
    'movies_ratings/assets/stylesheets/css/*.css',
    'movies_ratings/assets/js/scripts/*.js',
    'movies_ratings/assets/js//scripts/*.js.map'
  ]);
});

// dev watch js & less
gulp.task('watch', function() {
  gulp.watch('movies_ratings/assets/stylesheets/less/*.less', ['less']);
  gulp.watch('movies_ratings/assets/js/src/*.js', ['scripts']);
});

// BUILD
gulp.task('default', ['clean'], function() {
    gulp.start('clean', 'less', 'scripts');
});
