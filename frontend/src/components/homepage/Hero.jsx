import React from "react";
import Heroimage from "../../assets/hero-image-3.png";
import Typed from 'typed.js';

function Typedjs(props) {
  // Create reference to store the DOM element containing the animation
  const el = React.useRef(null);

  React.useEffect(() => {
    const typed = new Typed(el.current, {
      strings: props.strings,
      typeSpeed: props.typeSpeed,
      smartBackspace: props.smartBackspace
    });

    return () => {
      // Destroy Typed instance during cleanup to stop animation
      typed.destroy();
    };
  }, []);

  return (
    <div className={props.className}>
      <span ref={el} />
    </div>
  );
}

const Hero = () => {
  return (
    <div className="max-w-[1240px] py-16 sm:mt-8 md:mx-auto grid lg:grid-cols-5 bg-[#fff2f1] sm:rounded-xl">
      {/* TEXT*/}
      <div className="mb-8 col-span-2   w-full  text-black max-h-[600px] flex flex-cols-2 justify-center">
        <div className="max-w-[1240px] px-2 sm:px-16 w-full mx-auto flex flex-col justify-center">
          <p className="my-2 text-black font-bold text-center text-sm px-2 py-1 rounded-full w-[180px]  bg-[#d9c9ff]">
            We have price for you
          </p>
          <h1 className="text-5xl font-bold mb-4">
            Discover right price for used
          </h1>
          <Typedjs
            strings={["iPhone 13 Pro", "iPhone 8 Plus", "iPhone 12 Pro Max"]}
            typeSpeed={120}
            smartBackspace={120}
            loop
            className="text-4xl font-bold text-[#93123f]"
          />

          <p className="md:text-1xl text-sm uppercase font-bold text-black/60 mt-8">
            Get the best-in-class group mentoring plans
          </p>
          <p className="md:text-1xl text-sm uppercase font-bold text-black/60 ">
            and professional benefits for your team
          </p>
          <div className="flex mt-8 gap-4">
            <button className="bg-[#93123f] text-Black flex w-[160px] items-center py-2 rounded-md">
              <span className="mx-auto font-medium text-white text-center">
                BROWSE
              </span>
            </button>
          </div>
        </div>
      </div>

      <div className=" col-span-3 flex flex-col justify-center  items-center">

        <img className="w-fill lg:w-[90%] p-2 sm:p-0 mx-auto" src={Heroimage} alt="/" />

      </div>
    </div>
  );
};

export default Hero;
