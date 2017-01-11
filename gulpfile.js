var gulp = require('gulp'),
    cssnano = require('gulp-cssnano'),
    uglify = require('gulp-uglify'),
    del = require('del'),
    less = require('gulp-less'),
    path = require('path'),
    sourcemaps = require('gulp-sourcemaps');

// build less
gulp.task('less', function () {
  return gulp.src('leto_test/assets/stylesheets/less/*.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less') ]
    }))
    .pipe(cssnano())
    .pipe(gulp.dest('leto_test/assets/stylesheets/css'))
});

// build js
gulp.task('scripts', function() {
  return gulp.src('leto_test/assets/js/src/*.js')
    .pipe(sourcemaps.init())
      .pipe(uglify())
      .pipe(sourcemaps.write('/'))
    .pipe(gulp.dest('leto_test/assets/js/scripts'))
});

// clean js & css dirs
gulp.task('clean', function() {
    return del(['leto_test/assets/stylesheets/css/*.css',
                'leto_test/assets/js/scripts/*.js',
                'leto_test/assets/js//scripts/*.js.map']);
});

// dev watch js & less
gulp.task('watch', function() {
  gulp.watch('leto_test/assets/stylesheets/less/*.less', ['less']);
  gulp.watch('leto_test/assets/js/src/*.js', ['scripts']);
});

// BUILD
gulp.task('default', ['clean'], function() {
    gulp.start('clean', 'less', 'scripts');
});
