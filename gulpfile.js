var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function() {
    gulp.src('static_src/scss/app.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/css'))
});


gulp.task('sass:watch', function(){
  gulp.watch('static_src/scss/**/*.scss', ['sass']);
  // Other watchers
});

gulp.task("build", ["sass"]);