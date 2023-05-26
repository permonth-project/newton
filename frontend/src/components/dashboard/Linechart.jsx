import { ResponsiveLine } from "@nivo/line";


const commonProperties = {
    width: 900,
    height: 400,
    margin: { top: 20, right: 20, bottom: 60, left: 80 },
    animate: true,
    enableSlices: 'x',
}

const LineChart = ({ priceData, priceMin, priceMax }) => {
    return (
        <ResponsiveLine
            {...commonProperties}
            curve="monotoneX"
            data={priceData}
            xScale={{
                type: 'time',
                format: '%Y-%m-%d',
                useUTC: false,
                precision: 'day',
            }}
            xFormat="time:%Y-%m-%d"
            yScale={{
                type: 'linear',
                min: priceMin - 20,
                max: priceMax + 20
            }}
            axisLeft={{
                legend: 'linear scale',
                legendOffset: 12,
            }}
            axisBottom={{
                format: '%b %d',
                tickValues: 'every 14 days',
                legend: 'time scale',
                legendOffset: -12,
            }}
            enablePoints={true}
            pointSize={8}
            pointBorderColor="#fff"
            pointBorderWidth={2}
            useMesh={true}
            enableSlices={false}
            motionConfig='stiff'
            enableArea={true}
            areaBaselineValue={priceMin - 20}
        />
    );
};

export default LineChart;