
```bash
# Check for 60fps
./vsync-color.py "60"

# Check for 50fps
./vsync-color.py "50"
```

The work "vsync test" should be gray.

If you see it flash red or cyan, then a frame was displayed twice in a row.
There are multiple possible causes here;
 * The computer didn't render the frame in time.
 * The computer didn't deliver the frame in time.
 * The frame rate doesn't match the output.

The first two should hopefully be rare, while the last one is what we are
looking for.

This method was described at
http://www.vsynctester.com/manual.html#thenovelsolution
